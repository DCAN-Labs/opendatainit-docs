# Step 2: Preparing Data

## BIDS Standard Compliance
Make sure your data follows BIDS standards, including files such as `dataset_description.json` and a `README`. Any files that are required for the repository configuration with Amazon AWS that violate BIDS spec should be added to the file `.bidsignore`. For example, in the BOBS Repository, there are the files `index.html` and `V1.0.zip`: 

```
bobsrepository/
|__ sub-<LABEL>/
|   |__ ses-<AGE>mo/
|       |__ anat/
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-T1w.nii.gz
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-T1w.json
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-T2w.nii.gz
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-T2w.json
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-aseg_dseg.nii.gz
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-aseg_dseg.json
|
|__ phenotype/
|   |__ sessions.json
|   |__ sessions.tsv
|
|__ dataset_description.json
|__ dseg.tsv
|__ README.md
|__ index.html #.bigsignore
|__ V1.0.zip #.bigsignore
```

## `.gitattributes` Setup

The `.gitattributes` file needs to be properly set up mostly for OpenNeuro compatibility - see the section of their website on [Repository Conventions](https://docs.openneuro.org/git.html#repository-conventions):

> A dataset must always be present in the root level of the repository.

> OpenNeuro validates the size of regular git (non-annexed) files and a subset of bids-validation before accepting a git push. It is important to annex any large files in any commits before pushing. `.bidsignore` must always be a regular file. Some features are only available for regular files (such as diffing) and textual data is generally best kept as regular git objects.

> A recommended .gitattributes configuration for `git-annex` to automate annexing the correct files when using `git add` or `datalad save`
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

### Annex Backend (SHA256E vs MD5E)
OpenNeuro requires that you use SHA256E for the annex backend. `git-annex` assigns MD5E by default for S3, but other backends (SHA256E, SHA1E) also work for AWS, so you will need to specify this in the `.gitattributes` file with `* annex.backend=SHA256E` as shown above.

### Comparison of `annex.largefiles` Rules    
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

## Generate non-BIDS Files
For sharing via AWS, it's best to add:

1. A zip file that contains the full contents of the BIDS repository. This should only contain the files/folders relevant to the BIDS repository, so can exclude files like `.bidsignore` and `.gitignore` as well as `index.html`. This file enables users to quickly download the entire contents of the repository as a zip file via their browser by simply clicking on a link.
2. `index.html` file: This file is the interface for the repository on Amazon AWS. For instance, the BOBSRepository AWS page is here: [https://bobsrepository.s3.amazonaws.com/index.html](https://bobsrepository.s3.amazonaws.com/index.html). It allows you to browse the contents of the repo and also download the full contents (see **Download Entire Repository** button at the bottom of the page, which links to the zip file). The contents of the index.html file for this page can be viewed [here](index.html).

## Run BIDS Validation (TO DO)

Activate your conda environment:
```bash
module load conda
source activate datalad_BR
```

Use `deno` to run BIDS validation: `deno run -A jsr:@bids/validator <dataset path> > /path/to/denoresults.txt`

Address all ERRORS in the output. WARNINGS are suggestions and not required for validation, but ERRORS are required and will cause issues if not resolved.