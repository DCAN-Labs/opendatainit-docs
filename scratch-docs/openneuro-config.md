# OpenNeuro Compatibility Configuration

Proper configuration in order to connect your DataLad repository to OpenNeuro is described in their documentation on the page [Git access to OpenNeuro datasets](https://docs.openneuro.org/git.html). Below we provide additional information that users may find helpful for MIDB ODI DataLad repository setup. Note that this was written at a time when these OpenNeuro features were under active development (2024-2025) so may be out of date.

## .gitattributes
To make your DataLad repository compatible with OpenNeuro, you will need to add a `.gitattributes` file as described under [Repository Conventions](https://docs.openneuro.org/git.html#repository-conventions). This is needed for `git-annex` to automate annexing the correct files when using `git add` or `datalad save`:

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

##### Details: `* annex.backend=SHA256E`
OpenNeuro requires that you use SHA256E for the annex backend. `git-annex` assigns MD5E by default for S3, but other backends (SHA256E, SHA1E) also work for AWS, so you will need to specify this in the `.gitattributes` file with `* annex.backend=SHA256E` as shown above.

##### Details: `annex.largefiles`
OpenNeuro requires that certain files, particularly large files, be annexed (vs. kept as regular git files). Since we have already converted your repository to a DataLad repository, this step will already be complete! In addition, certain files are required to be kept as regular git files (e.g. `.bidsignore`). By default, DataLad does not annex these types of files, so this shouldn't be an issue for you either.




. This is specified in `.gitattributes` by `annex.largefiles` as follows:
 
- `annex.largefiles=nothing`: File is always stored in Git, never annexed *(e.g. `README`, `dataset_description.json`, `.bidsignore`)*
- `annex.largefiles.largerthan=1mb`: Files >1MB go into annex, smaller ones stay in Git *(e.g., all `.json` files smaller than 1mb)*
- `annex.largefiles=anything`: File is always stored in annex, no matter the size *(e.g., `phenotype/*.tsv` files)*

## BIDS Validation

OpenNeuro validates the size of regular git (non-annexed) files and a subset of bids-validation before accepting a `git push`. Datasets will not be published to OpenNeuro without fully passing BIDS validation. Our datasets are generally BIDS valid, and you may end up adding more files to your repository as part of the process of submitting to the MIDB ODI, so feel free to skip this step for now if you are already familiar with BIDS. 

Otherwise, we recommend running BIDS validation (e.g. the standard [BIDS Validator](https://bids-standard.github.io/bids-validator/)):

- `ERRORS` must be fixed
- `WARNINGS` are optional/suggestions for best practice, so can be safely ignored if not applicable to your data (and/or listed as a future continuous improvement item for your dataset)