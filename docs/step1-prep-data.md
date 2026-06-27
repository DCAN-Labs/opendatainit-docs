> **⚠️ WARNING**
> The current workflow is for smaller datasets only - [see details](datalad-init.md#note-for-small-data-repositories-only). The workflow will be adapted for larger datasets stored in MSI S3 buckets in the future

# Step 1: Data Preparation & General Requirements

## De-identification and Permission to Share Publicly
Make sure that the dataset can be shared publicly without violating HIPAA or data use agreements! You may need to perform de-identification, including defacing, for MRI. See [CDNI Brain](https://cdnis-brain.readthedocs.io/deidentification/#de-identification-of-mri-image-data) documentation for more information on how to perform defacing and other de-identification methods such as DICAT.

## Decide on Name of Repository
It's important to settle on a repository name early on as the name must be consistent when going through the multiple stages of setup (local project folder name, configuration files, github repository, etc.). The name should be simple and straightforward to describe what the contents of the data are. For example, the name of the Baby Open Brain (BOBs) Repository is `bobsrepository`.

## Create Project Folder on MSI Tier1 

- **Create a project folder containing your data on MSI tier 1 - the name of the folder must match the repository name you decided on above**
- **Store a backup of this source folder in an S3 bucket on MSI tier** - 
This folder will be converted to a DataLad repository that will serve as the source data for shared data. Sometimes DataLad configuration gets messed up and you essentially need to rebuild the repository from scratch, so it's critical that you have a totally separate additional source folder that is never touched that you can always recover from.

## BIDS formatting & validation

- The entire project folder must follow the [Brain Imaging Data Structure](https://bids-specification.readthedocs.io/en/stable/) standard.  
- We recommend running BIDS validation to be thorough (e.g. the standard [BIDS Validator](https://bids-standard.github.io/bids-validator/)).
- All validation `ERRORS` must be addressed. In contrast, `WARNINGS` are suggestions and not requirements to pass BIDS validation.
- If there are files in your project folder that violate BIDS validation, but are necessary to include, add them to a `.bidsignore` file.
