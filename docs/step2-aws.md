# Step 2: Create Amazon AWS S3 Bucket

The process for creating/submitting a new repository to Amazon AWS is slightly unusual, but the steps are fairly simple. We recommend following the adapted instructions provided below as part of the steps have already been completed for you as part of the MIDB ODI resource. However, for further guidance, please see the AWS [open-data-registry](https://github.com/awslabs/open-data-registry) repository README on Github, which also includes a video tutorial of this process - ([Adding your dataset to the Registry of Open Data on AWS](https://youtu.be/5nocWdjN1DA)). 

## Initiate Creation of the Amazon AWS Bucket

All data MIDB ODI repositories live under the MIDB departmental AWS account managed by the Informatics Hub. Please contact Lucille Moore, who can facilitate connecting you with the Informatics Hub to initiate the process of requesting a new data repository setup, i.e. a new S3 bucket on Amazon AWS. You do not need to have everything figured out/complete before doing this, it just allows Informatics time to connect with Amazon so that they know to expect a new submission from us for when you are ready to [submit a pull request](#submit-pull-request) to Amazon for review.

## Sync Existing Fork Under DCAN-Labs 
Normally the first step would be to create a fork of the AWS [open-data-registry](https://github.com/awslabs/open-data-registry) repository on Github. We already have an existing fork under the DCAN-Labs organization [here](https://github.com/DCAN-Labs/open-data-registry), so simply click **Sync fork** to update it fork from the central repository.

## Add a New YAML File for Your Repository
Nex you will create a new YAML file under `/datasets`. The general documentation provides an [example YAML](https://github.com/awslabs/open-data-registry#how-are-datasets-added-to-the-registry), but we recommend simply making a copy of the [BOBs Repository YAML](https://github.com/DCAN-Labs/open-data-registry/blob/main/datasets/bobsrepository.yaml), updating the filename with the name of your repository (using the exact string you decided on in Step 1 - [Decide on Name of Repository](step1-prep-data.md#decide-on-name-of-repository)), and updating the contents from there.

**Tips for constructing YAML file using [BOBs Repository YAML](https://github.com/DCAN-Labs/open-data-registry/blob/main/datasets/bobsrepository.yaml) as the template:**

 - Do not modify values for: `ManagedBy`, `Region` (`Resources`), or `Type` (`Resources`)
 - For `Resources` > `ARN` and `Explore`: replace `bobsrepository` with your repository name
 - `License` - adding a license is recommended, otherwise can leave blank or follow the README example (`There are no restrictions on the use of this data`)
 - Follow standard YAML formatting to avoid errors, e.g. use quotation marks for [special characters](https://stackoverflow.com/a/22235064). Include quotations when in doubt. Formatting errors will also be caught during continuous integration (CI) after submitting your pull request and can be fixed easily at that stage.

### Create Tutorial  
Note that one of the YAML file fields is `DataAtWork` > `Tutorials`. You are required to provide a link to a “tutorial,” which for a data repository can simply be instructions on how to access and download the data or some other very minimal documentation. Some helpful examples include: 

- BOBSRepo - [View or Download the BOBS Repository](https://bobsrepository.readthedocs.io/data_access/) 
- [INDI tutorial](https://fcon_1000.projects.nitrc.org/indi/s3/index.html) (provides a basic explanation of the data format/organization and how to access via Cyberduck)

## Submit Pull Request
Once these steps are complete, submit a pull request (PR) to the central repository and notify Lucille Moore and/or the Informatics Hub, who will then coordinate with Amazon to link your repository to the MIDB account and fasttrack review/approval. After the PR is merged (this may take a few days), Amazon will create a S3 bucket for you on AWS (named as defined in your YAML file) and send AWS credentials with read/write access to you.

## AWS Bucket Configuration (OPTIONAL)

The Informatics Hub will complete most configurations required to make your bucket publicly accessible. However, you may want to enable additional features (e.g., fine-grained permissions or usage tracking) that require access to the AWS web console. To make these changes, you can either request Informatics (the "root" user) to apply them, or ask to be added as an [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) to access the AWS console directly.

#### Enable ACLs Under Object Ownership
Although AWS generally recommends using bucket policies instead of ACLs, this workflow requires ACLs to be enabled, e.g. check **ACLs enabled** under **Object Ownership**:

![](images/edit-object-ownership.jpg)

#### Update ACL Permissions
Even if your bucket is publicly accessible, individual object/file permissions may still block downloads. Updating ACLs ensures users can access your data. 

1. Go to **Permissions** tab  
2. Scroll down to **Access control list (ACL)**
3. Click **Edit** and check the **List** and **Read** boxes for: 
    - **Authenticated users groups** (anyone with an AWS account)
    - (Optional) **Everyone (public access)** if broader access is desired.  
4. Check **I understand the effects of these changes on my objects and buckets**
5. Click **Save changes**.

## Resources
 - [open-data-registry](https://github.com/DCAN-Labs/open-data-registry?tab=readme-ov-file#registry-of-open-data-on-aws)
 - [AWS Onboarding Handbook for Data Providers](https://assets.opendata.aws/aws-onboarding-handbook-for-data-providers-en-US.pdf)      
 - [AWS Samples](https://github.com/aws-samples/)  
 - [Youtube tutorial: adding your data to Registry of Open Data on AWS](https://www.youtube.com/watch?v=5nocWdjN1DA)


