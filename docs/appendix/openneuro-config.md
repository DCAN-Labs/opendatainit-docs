# OpenNeuro Compatibility Configuration

Note that the configuration required is somewhat extensive and may take some time for new users. OpenNeuro was under active development at the time this was written, so it's possible these steps will be simplified as well. 

## .gitattributes Setup
The `.gitattributes` file needs to be properly set up mostly for OpenNeuro compatibility - see the section of their website on [Repository Conventions](https://docs.openneuro.org/git.html#repository-conventions):

- A dataset must always be present in the root level of the repository.

- OpenNeuro validates the size of regular git (non-annexed) files and a subset of bids-validation before accepting a git push. It is important to annex any large files before pushing. `.bidsignore` must always be a regular file. Some features are only available for regular files (such as diffing) and textual data is generally best kept as regular git objects.

- A recommended `.gitattributes` configuration for `git-annex` to automate annexing the correct files when using `git add` or `datalad save`:
```
* annex.backend=SHA256E
**/.git* annex.largefiles=nothing
*.bval annex.largefiles=nothing
*.bvec annex.largefiles=nothing
*.json annex.largefiles=largerthan=1mb
phenotype/*.tsv annex.largefiles=anything
*.tsv annex.largefiles=largerthan=1mb
dataset_description.json annex.largefiles=nothing
.bidsignore annex.largefiles=nothing
CHANGES annex.largefiles=nothing
README* annex.largefiles=nothing
LICENSE annex.largefiles=nothing
```

#### Annex Backend (SHA256E vs MD5E)
OpenNeuro requires that you use SHA256E for the annex backend. `git-annex` assigns MD5E by default for S3, but other backends (SHA256E, SHA1E) also work for AWS, so you will need to specify this in the `.gitattributes` file with `* annex.backend=SHA256E` as shown above.

#### Comparison of `annex.largefiles` Rules    
Depending on the file, OpenNeuro requires or recommends that files be git-annex files vs regular git files. This is specified in `.gitattributes` by `annex.largefiles` as follows:
 
**Convention:** `annex.largefiles=nothing`      
**Meaning:** File is always stored in Git, never annexed        
**Examples:** `README`, `dataset_description.json`, `.bidsignore`

**Convention:** `annex.largefiles.largerthan=1mb`      
**Meaning:** Files >1MB go into annex, smaller ones stay in Git.        
**Examples:** All `.json` files smaller than 1mb

**Convention:** `annex.largefiles=anything`      
**Meaning:** File is always stored in annex, no matter the size.        
**Examples:** `phenotype/*.tsv` files

## BIDS Validation

Datasets will not be published to OpenNeuro without fully passing BIDS validation. Our datasets are generally BIDS valid, and you may end up adding more files to your repository as part of the process of submitting to the MIDB ODI, so feel free to skip this step for now if you are already familiar with BIDS. 

Otherwise, we recommend running BIDS validation (e.g. the standard [BIDS Validator](https://bids-standard.github.io/bids-validator/)):

- `ERRORS` must be fixed
- `WARNINGS` are optional/suggestions for best practice, so can be safely ignored if not applicable to your data (and/or listed as a future continuous improvement item for your dataset)