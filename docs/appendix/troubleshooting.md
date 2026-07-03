# Troubleshooting
---

## Conda Environment Setup

**If having trouble with [Step 3: Set up DataLad Repository](../sop/step3-datalad.md):**

There are specific version requirements for `datalad` and `git annex` to be able to [set up Amazon S3 as a special remote](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#). If the central CDNI-wide conda environment doesn't work, check whether the package versions meet the requirements in the DataLad documentation. If not, you will want to create your own environment. 

### Create New Conda Env

Intructions for how to set up your own conda environment can also be found on [CDNI BRAIN](https://cdnis-brain.readthedocs.io/vscode/#conda-environments). For DataLad, decide on a unique name for your environment so you don't get it confused with the existing CDNI `datalad` environment  (e.g. could include your x500, `datalad_lmoore`).

```
# Create new conda env
source /projects/standard/faird/shared/code/external/envs/miniconda3/load_miniconda3.sh
conda create --name {ENV NAME}     
conda activate {ENV NAME}

# Activate and install dependencies
source activate my_datalad_env
conda install -c conda-forge datalad
conda install -c conda-forge git-annex=*=alldep*
```

The `git-annex` install of the standard distribution above (with `git-annex=*=alldep*`) will allow you to use the `signature=v4` flag in git annex `initremote` commands, which is required for the workflow to work correctly (basically this allows you to display the files in the public repo using human-readable filenames instead of hashes).


<!-- As of July 2026, the current package versions for the central CDNI `datalad` environment on MSI are:

**DataLad Packages**

| Name              | Version | Build        | Channel     |
| ----------------- | ------- | ------------ | ----------- |
| datalad           | 0.17.8  | pypi_0       | pypi        |
| datalad-container | 1.1.4   | pyhd8ed1ab_0 | conda-forge |
| datalad-installer | 0.3.1   | pypi_0       | pypi        |


**git-annex Package**

| Name      | Version     | Build            | Channel     |
| --------- | ----------- | ---------------- | ----------- |
| git-annex | 10.20250828 | nodep_h1234567_0 | conda-forge |
 -->


---

## Starting from Scratch
This should be avoided of course, but if you need to delete your DataLad repository and remake it due to errors in configuration that can't be resolved, remember to delete all of the following:

- GitHub repo - do not create a new one after deleting: this will be done automatically as part of the configuration process
- DataLad repository on MSI/local (if you get permission denied, change permissions and then delete)
- Amazon AWS contents 

**NEVER DELETE ORIGINAL SOURCE DATA STORED OUTSIDE OF THE DATALAD REPOSITORY**

---

## Public Accessibility Issues

The Informatics Hub will handle the majority of the configurations required to make the bucket publicly available. The first repository set up as part of MIDB ODI (BOBSRepository) required some additional configuration - these may or may not be needed for you, but are described below as potential solutions in case helpful. 

We recommend consulting with Informatics as to whether these updates would be appropriate. The updates described below must be made via the AWS web console accessible to Informatics. If you prefer to make the updates yourself, Informatics can add you as an [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) for you to access the AWS web console directly. 

<!-- The following are recommended configurations to ensure public accessibility and allow tracking for repository usage: -->

#### Enable ACLs Under Object Ownership
Although AWS generally recommends using bucket policies instead of ACLs, enabling ACLs is one way to deal with potential public accessibility issues (e.g. this was required in order for users to be able to download the zip file directly from their browser). To enable ACLs, check **ACLs enabled** under **Object Ownership**:

![](../images/edit-object-ownership.jpg)


#### Update ACL Permissions
Even if your bucket is publicly accessible, individual object/file permissions may still block downloads. Updating ACLs ensures users can access your data. 

1. Go to **Permissions** tab  
2. Scroll down to **Access control list (ACL)**
3. Click **Edit** and check the **List** and **Read** boxes for: 
    - **Authenticated users groups** (anyone with an AWS account)
    - (Optional) **Everyone (public access)** if broader access is desired.  
4. Check **I understand the effects of these changes on my objects and buckets**
5. Click **Save changes**.



