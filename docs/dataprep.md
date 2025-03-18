# Preparing Data

## Make Folder for DataLad Repository
If you haven’t already, make a directory for your DataLad repo: the name of the folder should match the name of your repository (e.g. the name of the bobsrepository DataLad folder is `bobsrepository`). Add the contents you would like to include and adjust as needed based on the rest of this page.

## BIDS Standard
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

### Running BIDS Validation
When your folder is fully set up, make sure to run BIDS validation as a final check. Also remember to run BIDS validation after adding any additional files needed (e.g. `index.html` and a zip file - see [Amazon AWS Configuration](#amazon-aws-configuration))
```bash
# Activate your conda environment:
module load conda
source activate datalad_BR

# Run BIDS validation with deno:
deno run -A jsr:@bids/validator <dataset path> > /path/to/denoresults.txt
```
Address all ERRORS in the output. WARNINGS are suggestions and not required for validation, but ERRORS are required to be addresseed and will cause issues if not resolved.

--------------------

## De-identification and Permission to Share Publicly
Perhaps it goes without saying, but first make sure that the dataset actually CAN be shared publicly without violating HIPAA or data use agreements! It’s possible you may have to perform some additional steps to de-identify the data, which may include defacing (see documentation on CDNI’s Brain or more extensive documentation for infant data defacing here), using DICAT to anonymize DICOMs before conversion/processing, and/or other tools. Please see [this page](https://cdnis-brain.readthedocs.io/deidentification/#de-identification-of-mri-image-data) on CDNI's Brain for more information on how to perform defacing and other de-identification.

--------------------

## OpenNeuro Compatibility Configuration
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

---------------

## Amazon AWS Configuration
For sharing via AWS, it's best to add:

1. A zip file that contains the full contents of the BIDS repository. This should only contain the files/folders relevant to the BIDS repository, so can exclude files like `.bidsignore` and `.gitignore` as well as `index.html`. This file enables users to quickly download the entire contents of the repository as a zip file via their browser by simply clicking on a link.
2. `index.html` file: This file is the interface for the repository on Amazon AWS. For instance, the BOBSRepository AWS page is here: [https://bobsrepository.s3.amazonaws.com/index.html](https://bobsrepository.s3.amazonaws.com/index.html). It allows you to browse the contents of the repo and also download the full contents (see **Download Entire Repository** button at the bottom of the page, which links to the zip file). The contents of the index.html file for this page can be viewed [here](https://github.com/DCAN-Labs/bobsrepository/blob/main/index.html).

Note that these files are not BIDS spec, and so will need to be added to `.bidsignore` as noted above ([BIDS Standard](#bids-standard)).

