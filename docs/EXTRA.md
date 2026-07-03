# EXTRA INFO TO POTENTIALLY ADD (copied from older RTDs version)

## Initialize & Configure DataLad Repository

NOTE: For Small Data Repositories Only
This SOP is designed for small repositories (e.g., <10 GB) that can be reasonably downloaded as a zip file via a web browser.

Larger neuroimaging datasets often contain hundreds to thousands of subjects, making it impractical to download the entire dataset at once. Instead, large datasets should be structured differently, employing dataset hierarchies to create [subdatasets/submodules](https://docs.datalad.org/en/stable/generated/man/datalad-subdatasets.html) for each subject folder. Large repositories also typically have their source data stored in [tier 2 storage](https://msi.umn.edu/our-resources/knowledge-base/stratus-faqs/what-tier-2-storage)

For guidance on handling large datasets, please refer to the adapted workflow in the [internal documentation](https://docs.google.com/document/d/1qEC6YwhW-kik2z1EZAlhhUgNSrgH9XlweW-avR00Yls/edit?usp=sharing).







## CAN LEAVE OUT FOR NOW


### Store AWS Credentials & GitHub Token (Optional)

Once your AWS S3 bucket is generated ([Step 2](aws.md)), the Informatics Hub will provide you with the necessary credentials for access, including AWS access and secret keys. These credentials are distinct from those tied to your MSI x500 account.

To store these credentials in your home directory, create the file `.aws/fcpindi.sh` and update to include the following information:

This file should include the following variables, used by DataLad to [interact with AWS](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#prerequisites) and GitHub: 

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `DATALAD_CREDENTIAL_GH_TOKEN`

This way, whenever you activate the datalad conda environment, you can just run the following instead of defining them as environmental variables as decribed under [Set Environmental Variables](datalad.md#2-set-environmental-variables):

```bash
source ~/.aws/fcpindi.sh
```
