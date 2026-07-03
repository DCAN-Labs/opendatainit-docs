
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
