
# AWS Bucket Configuration Recommendations

The Informatics Hub will complete most configurations required to make your bucket publicly accessible. However, you may want to enable additional features (e.g., fine-grained permissions or usage tracking) that require access to the AWS web console. To make these changes, you can either request Informatics (the "root" user) to apply them, or ask to be added as an [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) to access the AWS console directly.

**Once the AWS bucket is created, you will then be able to connect your local DataLad repository to it for public sharing.**

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


