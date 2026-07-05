# Step 1: Data Preparation & General Requirements

!!! note "NOTE"
    The items below don't need to be completed in order. If you get stuck, feel free to move on to another section while waiting for assistance.

## Define Repository Name - `REPO_NAME`
Choose a single repository name that will be used consistently across all stages of this workflow (which we will refer to as `REPO_NAME` in this documentation). This name acts as a global identifier for your dataset and will be reused in multiple systems, including DataLad, GitHub, and AWS. Renaming later can be difficult and may require reconfiguration across these platforms. 

**Naming guidelines:**

 - Use S3 bucket naming standards, including:
    - Use lowercase letters only
    - Do not include spaces (use hyphens if needed, **not underscores**)
    - Avoid special characters (e.g., !, @, #)
 - Keep the name concise but descriptive
 - Ensure the name is **unique** (especially on GitHub as it will be used for the name of the annexed repository for DataLad)

For example, the Baby Open Brain (BOBs) Repository name is `bobsrepository`.

---

## De-identification & Permission to Share

!!! danger "Potentially high-effort and/or time-consuming item"

Ensure your dataset can be shared publicly without violating HIPAA or any data use agreements. This may include, for example, removing identifiable metadata (e.g. with DICAT) and defacing MRI images. See the [CDNI Brain](https://cdnis-brain.readthedocs.io/deidentification/#de-identification-of-mri-image-data) documentation for guidance on defacing and other de-identification methods.

---

## BIDS Formatting
Ensure your dataset follows the Brain Imaging Data Structure ([BIDS](https://bids-specification.readthedocs.io/en/stable/)) standard. **Be sure to add non-BIDS files (e.g., `index.html`, zip archives) to a `.bidsignore` file so that you don't run into BIDS validation errors down the line** (particularly if you are planning to integrate with OpenNeuro - [see details](../appendix/openneuro.md)).

---

## Create Project Folder (MSI Tier 1) & S3 Backup
 - Create a project folder on MSI Tier 1 containing your dataset with the folder name `REPO_NAME` ([see details](#define-repository-name-repo_name)).
 - **Store a separate, untouched backup of this folder in an MSI S3 bucket.** This backup will not be converted to a DataLad repository and is only to be used to recover the data if the DataLad setup becomes corrupted or needs to be rebuilt from scratch. This is your personal source bucket to use as a backup, so doesn't require special naming or configuration.

---

## AWS Helper Files
**These steps are optional, but highly recommended** as they are relatively simple improvements that do a lot to improve accessibility for users. 

1. **Create a .zip file of the entire repository** to allow one-click downloads via a browser (can exclude files like `.bidsignore` and `.gitignore`)

2. **Add `index.html` browser interface** for users to navigate folders, download individual files/folders, etc. - e.g. see the [BOBSRepo index](https://bobsrepository.s3.amazonaws.com/index.html) (underlying html structure is [here](https://github.com/DCAN-Labs/bobsrepository/blob/main/index.html) and can be used as a template if helpful).

---

## Final Checks

Review the items above to ensure that you have completed each one. In addition, we recommend running your repository through a BIDS validator, using either the standard [BIDS Validator](https://bids-standard.github.io/bids-validator/) or your preferred tool. This will help catch errors in case, for example, you added an `index.html` file and forgot to add it to `.bidsignore`. 

As a reminder, `ERRORS` must be fixed, whereas `WARNINGS` are optional/suggestions for best practice, so can be safely ignored if not applicable to your data (and/or listed as a future continuous improvement item for your dataset).
