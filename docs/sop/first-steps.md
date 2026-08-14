# First Steps

## Define `REPO_NAME`

**Choose a repository name to use across all stages and systems outlined this workflow (DataLad, GitHub, AWS), which we will refer to as `REPO_NAME` in this documentation.** This may seem trivial, but renaming later can be difficult and may require reconfiguration across platforms, so lock in on a name early on following these guidelines:

 - Names should be concise, but descriptive
 - Use S3 bucket naming standards, including:
    - Use lowercase letters only
    - Do not include spaces (use hyphens if needed, **not underscores**)
    - Avoid special characters (e.g., !, @, #)
 - Ensure the name is unique, e.g. on the DCAN-Labs GitHub (since we will use this name for creating the annexed GitHub repository)
 - Example repository names for current MIDB ODI datasets:
      - Infant 3T/7T Precision Imaging: `infant-3t-7t-precision-mri`
      - Baby Open Brain (BOBs) Repository: `bobsrepository`

---

## Submit AWS Open Data Sponsorship Application

See the submission form here - <https://application.opendata.aws/>. Below are recommended values for you to copy and paste or details/examples for a subset of the form fields. If you have questions, include them in your email in the next step.

- **Name of your institution**: University of Minnesota - Twin Cities
- **Website of your institution**: https://www.umn.edu
- **Name of dataset**: *e.g. current OID repositories names include "Baby Open Brains (BOBs) Repository on AWS" and "Infant 3T/7T Precision Imaging"*
- **Dataset license**: CC-By Attribution 4.0 International
- **URL to documentation of the structure and content of the dataset**: *You should already have this available from putting together your YAML file - this can be a documentation site (e.g. for BOBSRepository this information is contained in a ReadtheDocs site [here](https://bobsrepository.readthedocs.io/latest/data_access/#organization-of-the-bobs-repository-data)) or a simple README file (e.g. see Infant 3T/7T Precision Imaging [GitHub README](https://github.com/DCAN-Labs/infant_3T_7T_precision_imaging/tree/main#infant-3t7t-precision-imaging-data))*

---

## Contact Informatics Hub 

All MIDB ODI repositories are hosted under the MIDB AWS account managed by the Informatics Hub. We recommend emailing Thomas Pengo, Lucille Moore, and Damien Fair early on so that everyone is aware and on the same page about a new dataset being added to the MIDB ODI. In your email:

- Inform them that you are working on adding a new data repository to the MIDB Open Data Initiative
- Provide at least a single sentence overview of what the data are
- Request that a new S3 bucket be created on using `{REPO_NAME}` as the bucket name
- As a courtesy, it might be helpful to also mention what stage of the process you are on if you've made progress already in other areas - feel free to even link directly to the relevant page/section of this site

The Informatics Hub will then generate the S3 bucket for you under the MIDB AWS account and share credentials via Box that you will use to connect your DataLad repository (one of the final steps in this workflow - [Configure the S3 Special Remote](datalad.md#3-configure-the-s3-special-remote)).


