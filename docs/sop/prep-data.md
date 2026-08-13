# Step 1: Data Preparation & General Requirements

!!! note "NOTE"
    The items below don't need to be completed in order. If you get stuck, feel free to move on to another section while waiting for assistance.

## Define Repository Name (`REPO_NAME`)

**Choose a repository name to use across all stages and systems outlined this workflow (DataLad, GitHub, AWS), which we will refer to as `REPO_NAME` in this documentation.**

Renaming later can be difficult and may require reconfiguration across platforms, so lock in on a name early on following these guidelines:

 - Names should be concise, but descriptive
 - Use S3 bucket naming standards, including:
    - Use lowercase letters only
    - Do not include spaces (use hyphens if needed, **not underscores**)
    - Avoid special characters (e.g., !, @, #)
 - Ensure the name is **unique** (especially on GitHub as it will be used for the name of the annexed repository for DataLad)

For example, the Baby Open Brain (BOBs) Repository name is `bobsrepository`.

---

## De-identification & Permission to Share

!!! danger "Potentially high-effort and/or time-consuming item"
    This step can be complex as the rules vary by dataset, institution, IRB protocol, etc.

**Consult with stakeholders to ensure that your data can be shared publicly and update data as needed (e.g. defacing imaging data is often required).**

Ensure your dataset can be shared publicly without violating HIPAA or any data use agreements. This may include, for example, removing identifiable metadata (e.g. with DICAT) and defacing MRI images. See [CDNI Brain](https://cdnis-brain.readthedocs.io/deidentification/#de-identification-of-mri-image-data) documentation for guidance on defacing and other de-identification methods.

---

## BIDS Formatting

**Ensure that dataset adheres to Brain Imaging Data Structure ([BIDS](https://bids-specification.readthedocs.io/en/stable/)) standard.**

 - Add non-BIDS-compliant files (e.g., `index.html`, zip archives) to a `.bidsignore` file to avoid running into BIDS validation errors down the line *(particularly if you are planning to [integrate with OpenNeuro](../appendix/openneuro.md), which requires strict BIDS compliance)*
 - If in doubt, use the standard [BIDS Validator](https://bids-standard.github.io/bids-validator/) or other utility - fix all `ERRORS` (`WARNINGS` are optional/suggestions for best practice, so can be safely ignored if not applicable to your data)

---

## Create Tier1 Project Folder & S3 Backup

**Create a project folder on MSI Tier 1 AND a backup source folder (on Tier 1 or 2).**

 - Name this folder with your `REPO_NAME` ([see details](#define-repository-name-repo_name))
 - This project folder will be converted to a DataLad repository, so should include your BIDS data and AWS helper files (see next section) and nothing else 
 - **Store a separate, untouched backup of this folder elsewhere (e.g. in an MSI S3 bucket).** This backup will not be converted to a DataLad repository and is only to be used to recover the data if the DataLad setup becomes corrupted or needs to be rebuilt from scratch.

---

## AWS Helper Files

**Add zip file(s) and an `index.html` to make data download for users as simple as possible** 

This step is optional, but highly recommended as they are relatively simple improvements that do a lot to improve accessibility for users. 

- If your repository is small enough, create a .zip file of the entire repository to allow one-click downloads via a browser (can exclude files like `.bidsignore` and `.gitignore`)

- Add an `index.html` file to allow users to navigate folders and download data super easily. See the [BOBSRepo `index.html`](https://github.com/DCAN-Labs/bobsrepository/blob/main/index.html) as an example, which renders as <https://bobsrepository.s3.amazonaws.com/index.html>.

- Remember to add these files to `.bidsignore` to keep the data repo BIDS valid
