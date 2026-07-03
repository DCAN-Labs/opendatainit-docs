# Step 1: Data Preparation & General Requirements

**NOTE that the items below don't need to be completed in order. If you get stuck, just move on to another section while waiting on assistance.**

## 1. BIDS Formatting & Validation

Ensure your dataset follows the Brain Imaging Data Structure ([BIDS](https://bids-specification.readthedocs.io/en/stable/)) standard. Non-BIDS files (e.g., index.html, zip archives) can be added to a `.bidsignore` file. Note that strict BIDS adherence is required if you choose to link your repository to OpenNeuro after setting up the Amazon AWS repository (discussed later in this documentation).

## 2. De-identification & Permission to Share
Ensure your dataset can be shared publicly without violating HIPAA or any data use agreements. This may include, for example, removing identifiable metadata (e.g. with DICAT) and defacing MRI images. See the [CDNI Brain](https://cdnis-brain.readthedocs.io/deidentification/#de-identification-of-mri-image-data) documentation for guidance on defacing and other de-identification methods.

## 3. Choose a Repository Name
Select a clear, descriptive repository name early in the process. The name must remain consistent across all steps, including the local project folder, configuration files, GitHub repository name, etc. Keep it simple and descriptive. For example, the repo name for the Baby Open Brain (BOBs) Repository is `bobsrepository`.

## 4. Create Project Folder on MSI Tier 1
Create a project folder on MSI Tier 1 containing your dataset - **the folder name must match your repository name from the prior step.**

> ⚠️ **Critical: Create a Backup**
> Store a separate, untouched backup of this folder in an MSI S3 bucket. This backup should never be modified and will allow you to recover if the DataLad setup becomes corrupted or needs to be rebuilt.

## 5. AWS Helper Files (*Optional but highly recommended*)
These are relatively quick and simple improvements that do a lot to improve accessibility for users. If you need assistance, feel free to move on to next steps and follow up with Lucille Moore in the meantime. 

1. **Zip File for Full Download**: Create a .zip archive of the entire repository to allow one-click downloads via a browser. Include only relevant dataset contents (e.g. can exclude files like `.bidsignore` and `.gitignore`)

2. **Add `index.html` browser interface** to allow users to navigate folders, download individual files, and/or download the full dataset as a zip file. See
 [https://bobsrepository.s3.amazonaws.com/index.html](https://bobsrepository.s3.amazonaws.com/index.html) for example. The underlying code can be copied and modified as needed from [https://github.com/DCAN-Labs/bobsrepository/blob/main/index.html](https://github.com/DCAN-Labs/bobsrepository/blob/main/index.html).



