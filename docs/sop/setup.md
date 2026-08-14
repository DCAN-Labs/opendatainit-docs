# Set up Environment

## One-Time Setup Items

#### DataLad Conda Environment 

We recommend setting up your own Conda environment as you may run into access errors using the central CDNI `datalad` environment (`fatal: unable to access DCAN-Labs/{GIT REPO NAME}.git: Problem with the SSL CA cert (path? access rights?)`). Here is an example setup (choose a more unique name for `{ENV NAME}`, such as `datalad-{your x500}` so that you don't get it confused with the CDNI environment).

```bash
module load conda
conda create --name {ENV NAME}
source activate {ENV NAME}

conda install -c conda-forge datalad
conda install -c conda-forge git-annex=*=alldep*
```

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

Assuming you have completed the setup outlined above: moving forward, **before running any DataLad workflow** (e.g., updating a repository, creating a sibling, or configuring AWS), you will need to:

**Activate datalad conda environment**

```bash
module load conda

# If using your own datalad conda environment (recommended)
conda activate {ENV NAME}

# If using CDNI-wide datalad conda environment 
source /projects/standard/faird/shared/code/external/envs/miniconda3/load_miniconda3.sh
conda activate datalad
```

**Define required environmental variables**

Note: the Informatics Hub will provide you with AWS access and secret keys after creating the AWS bucket (see [First Steps](first-steps.md)), required to connect your DataLad repository to AWS as a special remote. Also note that these credentials are distinct from your MSI credentials for tier2 access.

```bash
# GitHub Token
export DATALAD_CREDENTIAL_GITHUB_TOKEN="{your-github-token}"

# AWS credentials
export AWS_ACCESS_KEY_ID="{access_key_id}"
export AWS_SECRET_ACCESS_KEY="{secret_access_key}"
```





