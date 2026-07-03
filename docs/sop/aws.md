# Step 2: Create an AWS S3 Bucket

Below we walk through how to submit a new repository to AWS. These steps have been adapted and simplified from the [AWS Open Data Registry README](https://github.com/awslabs/open-data-registry) to provide resources and streamlined workflows developed for MIDB ODI datasets. However, we still recommend reviewing the main AWS documentation as it provides a nice overview and additional information that you may find helpful if you get stuck, including a [video tutorial](https://youtu.be/5nocWdjN1DA).

## 1. Request a New S3 Bucket
All MIDB ODI repositories are hosted under the MIDB AWS account managed by the Informatics Hub. Contact Lucille Moore to initiate a request for a new S3 bucket. You do not need to have all details finalized, this step simply notifies Informatics and AWS in advance of your upcoming submission to help streamline connecting to the MIDB account and submission acceptance.

## 2. Sync the Existing Fork 
Instead of creating a new fork, use the existing DCAN-Labs fork: [https://github.com/DCAN-Labs/open-data-registry](https://github.com/DCAN-Labs/open-data-registry). **Click “Sync fork” to update it with the latest changes from the main repository.**

## 3. Create a YAML File
Add a new YAML file under `/datasets`. We recommend using the [BOBs Repository YAML](https://github.com/DCAN-Labs/open-data-registry/blob/main/datasets/bobsrepository.yaml) as a template. Make a copy, rename the file using your repository name (from Step 1), and update the contents accordingly.

#### Detailed YAML update guidelines

 - Do NOT modify the values for:
    - `ManagedBy`
    - `Region` (under `Resources`)
    - `Type` (under `Resources`)
 - `Resources` > `ARN` and `Explore`: replace `bobsrepository` with your repository name
 - `License` - optional, but recommended (either use template example or leave field blank)
 - Ensure valid YAML formatting, e.g. using quotes for [special characters](https://stackoverflow.com/a/22235064), or when unsure. Formatting errors will be flagged during CI after submitting the PR and can be easily fixed at that point as well

## 4. Add a Tutorial

The YAML field `DataAtWork` > `Tutorials` requires a link to a “tutorial." We recommend that, at minimum, this includes documentation on the contents and organization of the dataset (see [BOBSRepository Tutorial](https://bobsrepository.readthedocs.io/data_access/)).
 
## 5. Submit Pull Request
Once these steps are complete, submit a pull request to the main repository and notify Lucille Moore and the Informatics Hub, who will coordinate with AWS to link your repository to the MIDB account. After the PR is merged (this may take a few days), AWS will create the S3 bucket and Informatics will configure the bucket to give you read/write access.

!!! note "Recommended AWS Bucket Configuration"
    See [appendix](../appendix/aws-bucket-config.md) for recommended AWS bucket configurations.

