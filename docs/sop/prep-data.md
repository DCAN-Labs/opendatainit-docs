# Step 1: Data Preparation & General Requirements

!!! note "NOTE"
    The items below don't need to be completed in order. If you get stuck, feel free to move on to another section while waiting for assistance.

## Define Repository Name - `REPO_NAME`
<input type="checkbox"> *Decide on consistent repository name (`REPO_NAME`)*

Choose a single repository name that will be used consistently across all stages and systems involved in this workflow, including DataLad, GitHub, and AWS. Renaming later can be difficult and may require reconfiguration across these platforms, so we recommend deciding on a name early on, which we will refer to as `REPO_NAME` in this documentation. **Names should be concise, but descriptive, and follow these guidelines:**

 - Use S3 bucket naming standards, including:
    - Use lowercase letters only
    - Do not include spaces (use hyphens if needed, **not underscores**)
    - Avoid special characters (e.g., !, @, #)
 - Ensure the name is **unique** (especially on GitHub as it will be used for the name of the annexed repository for DataLad)

For example, the Baby Open Brain (BOBs) Repository name is `bobsrepository`.

---

## De-identification & Permission to Share

<input type="checkbox"> *Consult with stakeholders to ensure that your data can be shared publicly*      
<input type="checkbox"> *Update data as needed (e.g. defacing imaging data is often required)*

!!! danger "Potentially high-effort and/or time-consuming item"
    This step can be complex as the rules vary by dataset, institution, IRB protocol, etc.

Ensure your dataset can be shared publicly without violating HIPAA or any data use agreements. This may include, for example, removing identifiable metadata (e.g. with DICAT) and defacing MRI images. See the [CDNI Brain](https://cdnis-brain.readthedocs.io/deidentification/#de-identification-of-mri-image-data) documentation for guidance on defacing and other de-identification methods.

---

## BIDS Formatting

<input type="checkbox"> *Ensure that dataset adheres to BIDS standard* 

 - Datasets must adhere to the Brain Imaging Data Structure ([BIDS](https://bids-specification.readthedocs.io/en/stable/)) standard
 - Add non-BIDS-compliant files (e.g., `index.html`, zip archives) to a `.bidsignore` file to avoid running into BIDS validation errors down the line *(particularly if you are planning to [integrate with OpenNeuro](../appendix/openneuro.md), which requires strict BIDS compliance)*

---

## Create Tier1 Project Folder & S3 Backup

<input type="checkbox"> *Create folder on tier1 as well as a backup source folder on tier2*

 - Create a project folder on MSI Tier 1 containing your dataset with the folder name `REPO_NAME` ([see details](#define-repository-name-repo_name)).
 - **Store a separate, untouched backup of this folder in an MSI S3 bucket.** This backup will not be converted to a DataLad repository and is only to be used to recover the data if the DataLad setup becomes corrupted or needs to be rebuilt from scratch. This is your personal source bucket to use as a backup, so doesn't require special naming or configuration.

---

## AWS Helper Files

<input type="checkbox"> *Add zip file(s) and `index.html` to make data download for users as simple as possible* 

This step is optional, but highly recommended as they are relatively simple improvements that do a lot to improve accessibility for users. 

1. Create a .zip file of the entire repository to allow one-click downloads via a browser (can exclude files like `.bidsignore` and `.gitignore`)

2. Add `index.html` browser interface for users to navigate folders, download individual files/folders, etc. - e.g. see the [BOBSRepo index](https://bobsrepository.s3.amazonaws.com/index.html) (underlying html structure is [here](https://github.com/DCAN-Labs/bobsrepository/blob/main/index.html) and can be used as a template if helpful).

---

## Final Checks - BIDS Validation

<input type="checkbox"> *Run BIDS validation to perform final checks prior to converting to DataLad* 

Review the items above to ensure that you have completed each one. In addition, we recommend running your repository through a BIDS validator, using either the standard [BIDS Validator](https://bids-standard.github.io/bids-validator/) or your preferred tool. This will help catch errors in case, for example, you added an `index.html` file and forgot to add it to `.bidsignore`. 

As a reminder, `ERRORS` must be fixed, whereas `WARNINGS` are optional/suggestions for best practice, so can be safely ignored if not applicable to your data (and/or listed as a future continuous improvement item for your dataset).
