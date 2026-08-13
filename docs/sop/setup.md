# Step 3: Set up Environment

## One-Time Setup Items

#### Git Credentials 
See [DataLad documentation for configuring git credentials](https://handbook.datalad.org/en/latest/intro/installation.html#initial-configuration). Run the following commands in your home directory on MSI:

```bash
cd ~
git config --global --add user.name "Bob McBobFace"
git config --global --add user.email bob@example.com
```

#### Personal Access Token

You will need to create a personal access token on GitHub - see [GitHub documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens). **Your GitHub personal access token must have permissions to create repositories in the DCAN-Labs organization** - speak with the CDNI/DCAN operations staff, leadership, and/or CDNI project managers for assistance if you do not have access to the DCAN-Labs organization on GitHub.

---


## Before running any DataLad workflow

Assuming you have completed the setup outlined in **3.1** above: moving forward, **before running any DataLad workflow** (e.g., updating a repository, creating a sibling, or configuring AWS), you will need to:

!!! warning "Warning: Conda Environments"
    If you run into potential issues with the conda environment at any point, such as errors about incorrect package versions or commands not working as expected, see [Troubleshooting > Conda Environment Setup](../appendix/troubleshooting.md#conda-environment-setup).


**1. Activate the CDNI-wide datalad conda environment**

```bash
source /projects/standard/faird/shared/code/external/envs/miniconda3/load_miniconda3.sh
conda activate datalad
```

**2. Define required environmental variables**

```bash
# GitHub Token
export DATALAD_CREDENTIAL_GITHUB_TOKEN="{your-github-token}"

# AWS credentials
export AWS_ACCESS_KEY_ID="{access_key_id}"
export AWS_SECRET_ACCESS_KEY="{secret_access_key}"
```



