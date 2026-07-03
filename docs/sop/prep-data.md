# Step 1: Data Preparation & General Requirements

!!! note "NOTE"
    The items below don't necessarily need to be completed in order. If you get stuck, just move on to another section while waiting for assistance.

## BIDS Formatting

Ensure your dataset follows the Brain Imaging Data Structure ([BIDS](https://bids-specification.readthedocs.io/en/stable/)) standard. Non-BIDS files (e.g., index.html, zip archives) can be added to a `.bidsignore` file. Note that strict BIDS adherence is required if you choose to link your repository to OpenNeuro after setting up the Amazon AWS repository (discussed later in this documentation).

## De-identification & Permission to Share
Ensure your dataset can be shared publicly without violating HIPAA or any data use agreements. This may include, for example, removing identifiable metadata (e.g. with DICAT) and defacing MRI images. See the [CDNI Brain](https://cdnis-brain.readthedocs.io/deidentification/#de-identification-of-mri-image-data) documentation for guidance on defacing and other de-identification methods.

## Define Repository Name
Select a clear, descriptive repository name early in the process. The name must remain consistent across all steps, including the local project folder, configuration files, GitHub repository name, etc. Keep it simple and descriptive. For example, the repo name for the Baby Open Brain (BOBs) Repository is `bobsrepository`.

## Create Project Folder (MSI Tier 1)
Create a project folder on MSI Tier 1 containing your dataset - **the folder name must match your repository name from the prior step.**

!!! warning "Warning: Create Backup to S3"
    Store a separate, untouched backup of this folder in an MSI S3 bucket. This backup should never be modified and will allow you to recover if the DataLad setup becomes corrupted or needs to be rebuilt.

## AWS Helper Files
**These steps are optional, but highly recommended** as they are relatively simple improvements that do a lot to improve accessibility for users. 

1. **Create a .zip file of the entire repository** to allow one-click downloads via a browser (can exclude files like `.bidsignore` and `.gitignore`)

2. **Add `index.html` browser interface** for users to navigate folders, download individual files/folders, etc. - e.g. see the [BOBSRepo index](https://bobsrepository.s3.amazonaws.com/index.html) (underlying html structure is [here](https://github.com/DCAN-Labs/bobsrepository/blob/main/index.html) and can be used as a template if helpful).


<!-- ### How to run BIDS validation
When your folder is fully set up, run BIDS validation as a final check. Also remember to run BIDS validation after adding any additional files needed (e.g. `index.html` and a zip file - see [Amazon AWS Configuration](#amazon-aws-configuration))
```bash
module load conda
source activate datalad_BR
deno run -A jsr:@bids/validator <dataset path> > /path/to/denoresults.txt
``` -->



