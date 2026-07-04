# Step 2: Create an AWS S3 Bucket

Below we walk through how to submit a new repository to AWS. These steps have been adapted and simplified from the [AWS Open Data Registry README](https://github.com/awslabs/open-data-registry) to provide resources and streamlined workflows developed for MIDB ODI datasets. However, we still recommend reviewing the main AWS documentation as it provides a nice overview and additional information that you may find helpful if you get stuck, including a [video tutorial](https://youtu.be/5nocWdjN1DA).

## Request a New S3 Bucket
All MIDB ODI repositories are hosted under the MIDB AWS account managed by the Informatics Hub. Contact Lucille Moore to initiate a request for a new S3 bucket. You do not need to have all details finalized, this step simply notifies Informatics and AWS in advance of your upcoming submission to help streamline connecting to the MIDB account and submission acceptance.

## Sync the Existing Fork 
Instead of creating a new fork, use the existing DCAN-Labs fork: [https://github.com/DCAN-Labs/open-data-registry](https://github.com/DCAN-Labs/open-data-registry). **Click “Sync fork” to update it with the latest changes from the main repository.**

## Create a YAML File
To register your dataset in the Open Data Registry, add a new YAML file under `/datasets` with information specific to your data repository. We recommend copying the [BOBs Repository YAML](https://github.com/DCAN-Labs/open-data-registry/blob/main/datasets/bobsrepository.yaml) as a starting template. Rename the file to match your repository name and update the fields accordingly.

The YAML file will be used to generate the summary page for your repository on AWS. For example, the information displayed for BOBSRepo on [https://registry.opendata.aws/bobsrepository/](https://registry.opendata.aws/bobsrepository/) is sourced from the YAML within the main AWS repository [here](https://github.com/awslabs/open-data-registry/blob/main/datasets/bobsrepository.yaml).

!!! note "General Note"
      The YAML does not need to be perfect on your first attempt. Mistakes in formatting or missing required fields will be flagged by CI checks when you submit the PR and can be resolved at that point.

### Guidance

 - **File naming:** Ensure the filename exactly matches the repository name you defined in Step 1.
 - **Review required fields:** See the [AWS Open Data Registry README](https://github.com/awslabs/open-data-registry#how-are-datasets-added-to-the-registry) for a full list of required and optional fields and descriptions
 - **Required field values for MIDB ODI**: use the following values for these fields (as displayed in the BOBSRepo YAML), except to replace `{YOUR REPO NAME}` with the name of your repository (again needs to match what you decided in Step 1 exactly)

```
ManagedBy: Masonic Institute for the Developing Brain (MIDB) Open Data Initiative

Resources:
- Description: 
   ARN: arn:aws:s3:::{YOUR REPO NAME}
   Region: us-east-2
   Type: S3 Bucket
   Explore:
   - '[Browse Bucket](https://{YOUR REPO NAME}.s3.amazonaws.com/index.html)'
```

 - **YAML formatting**: use valid YAML formatting, such as wrapping text containing [special characters](https://stackoverflow.com/a/22235064) in quotes. You can validate your YAML using online tools such as [https://jsonformatter.org/yaml-validator](https://jsonformatter.org/yaml-validator)
 - **"Tutorials"**: The `DataAtWork` > `Tutorials` fields can point to a tutorial, tool, application, or publication that uses the data. If you are unsure, simply link to documentation describing the dataset structure, which should be provided for users regardless (e.g., a README, ReadTheDocs page, or an `index.html` file). Again see the BOBSRepo YAML file as an example.
 
---

## Submit Pull Request
Once these steps are complete, submit a pull request to the main repository and notify Lucille Moore and the Informatics Hub, who will coordinate with AWS to link your repository to the MIDB account. After the PR is merged (this may take a few days), AWS will create the S3 bucket and Informatics will configure the bucket to give you read/write access.
