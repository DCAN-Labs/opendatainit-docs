
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



<!-- ### How to run BIDS validation
When your folder is fully set up, run BIDS validation as a final check. Also remember to run BIDS validation after adding any additional files needed (e.g. `index.html` and a zip file - see [Amazon AWS Configuration](#amazon-aws-configuration))
```bash
module load conda
source activate datalad_BR
deno run -A jsr:@bids/validator <dataset path> > /path/to/denoresults.txt
``` -->

