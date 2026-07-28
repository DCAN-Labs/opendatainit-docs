# Step 3: Set up DataLad Repository

This guide walks through setting up DataLad using BOB's Repository as an example, including creating a sibling GitHub repository to store metadata for provenance and configuring Amazon S3 as a special remote for public data sharing. 

---

## 3.1 Initial Setup & Conda Environment

### Configure Git Credentials 
Make sure your [git credentials are configured](https://handbook.datalad.org/en/latest/intro/installation.html#initial-configuration). This will be required when creating the sibling GitHub repository. **THIS ONLY NEEDS TO BE DONE ONCE.**

```bash
cd ~
git config --global --add user.name "Bob McBobFace"
git config --global --add user.email bob@example.com
```

### Create Personal Access Token

You will need to create a personal access token on GitHub in order to create the GitHub sibling repo for annexation ([see details](#create-github-sibling)) - see instructions on the [GitHub documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens). **Your GitHub personal access token must have permissions to create repositories in the DCAN-Labs organization** - speak with the CDNI/DCAN operations staff, leadership, and/or CDNI project managers for assistance if you do not have access to the DCAN-Labs organization on GitHub.

### Activate Conda Environment
Activate the CDNI-wide datalad conda environment: 

```bash
source /projects/standard/faird/shared/code/external/envs/miniconda3/load_miniconda3.sh
conda activate datalad
```

!!! warning "Warning: Conda Environments"
    If you run into potential issues with the conda environment at any point, such as errors about incorrect package versions or commands not working as expected, see [Troubleshooting > Conda Environment Setup](../appendix/troubleshooting.md#conda-environment-setup).

---

## 3.2 Initialize DataLad Repository 

Go to your project folder, initialize datalad, and save:
```bash
cd /path/to/{REPO_NAME}
datalad create --force
datalad save -m "initial commit"
```

- `--force` is necessary for non-empty folders
- `datalad save` basically combines `git commit` and `git push` commands
- Use `datalad status` command as needed to make sure local changes are tracked

---

## 3.3 Create GitHub Sibling Repository

Next, we will have DataLad create an empty dataset repository on GitHub where the data will be annexed.

### Set GitHub Token as Environmental Variable

First set your GitHub personal access token (that you generated in [this step](#create-personal-access-token)) as an environmental variable. DataLad specifically supports credentials through an environment variable named `DATALAD_CREDENTIAL_<CREDENTIAL-NAME>_TOKEN`, so `--credential github` used to create the GitHub sibling in the next step corresponds to `DATALAD_CREDENTIAL_GITHUB_TOKEN`. **Set your GitHub personal access token as an environmental variable like so:**

```
export DATALAD_CREDENTIAL_GITHUB_TOKEN='paste-your-github-token-here'
```

### Generate GitHub Sibling

To create the GitHub sibling, run:

```bash
datalad create-sibling-github -d . DCAN-Labs/{REPO_NAME} --credential github
```

You can confirm the creation of the sibling (named github) with the `datalad siblings` command:
```bash
$ datalad siblings
.: here(+) [git]
.: github(-) [https://github.com/DCAN-Labs/{REPO_NAME}.git (git)]
```

## 3.3 Connect to AWS S3

### Set Environmental Variables
Once your AWS S3 bucket is generated, AWS access and secret keys will be provided to you by the Informatics Hub. **Note that these credentials are distinct from your MSI credentials and are required for using Amazon AWS as a special remote.** 

Activate your conda environment (if you haven't already) and set your AWS access and secret keys as environmental variables in order to be able to push changes to AWS:

```bash
# Set AWS credentials as environmental variables
export AWS_ACCESS_KEY_ID="<access_key_id>"
export AWS_SECRET_ACCESS_KEY="<secret_access_key>"
```

### Add Amazon S3 as Special Remote
The process for adding an Amazon S3 as a special remote is described in the DataLad Handbook - see [Walk-through: Amazon S3 as a special remote](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#).

The default behavior of DataLad is to name files with MD5 hashes, which are used by `git-annex` under the hood to manage file versioning. The drawback to this is that the filenames are no longer human-readable unless users download the data via DataLad, which may be an unnecessary barrier to users for data access. We therefore recommend using additional flags when linking the repository to the special remote (`exporttree=yes` and `versioning=yes`). The flags `exporttree=yes` and `versioning=yes` use the original file names instead of replacing them with MD5 hashes. Because MD5 hashes are used for version control, the first flag used in isolation will cause you to lose the direct linkage to the hash-based versioning system, overwriting and removing access to older file versions. The flag `versioning=yes` is therefore required in order to preserve prior file versions on AWS.

To add Amazon S3 as a special remote, use the following command:
```bash
git annex initremote aws type=S3 encryption=none bucket={REPO_NAME} /
autoenable=true signature=v4 datacenter=us-east-2 public=yes exporttree=yes versioning=yes
```

Set bucket URL for git-annex to be able to download files from the bucket without requiring your AWS credentials:
```bash
git annex enableremote aws publicurl="https://{REPO_NAME}.s3.amazonaws.com”
```

---

## 3.4 Update GitHub sibling configuration

Once the Amazon S3 has been added as a special remote, you will next update the dependencies for your GitHub sibling repository with the flag `--publish-depends aws`. This flag sets a publication dependency so that whenever you push your changes, the annexed contents are first pushed to the special remote and then GitHub (so that the information is updated/annexed across platforms):

```bash
datalad siblings configure \
    -d . \
    -s github \
    --publish-depends aws
```

## 3.5 Publish
Push updated file contents and data provenance for versioning to S3 and Github. The first command is required when using the `exporttree=yes` flag for special remotes. Also note that you may have to enter your GitHub credentials a few times with the final command:

```bash
git annex export main --to aws
datalad push --to github
```

You should now be able to see the updated files on S3 and symlinks in Github (these are not the files, but rather symbolic links to annexed data on the S3 remote).


## Environmental Setup: Quick Tips

In cases where you need to update your DataLad repository or pick up from a certain stage of the repository setup, etc. remember to always activate the `datalad` conda environment and set the appropriate environmental variables like so (this documentation assumes that you have completed all of the necessary setup described above):


**1. Activate the CDNI-wide datalad conda environment**

```bash
source /projects/standard/faird/shared/code/external/envs/miniconda3/load_miniconda3.sh
conda activate datalad
```

**2. Set Environmental Variables**

```bash
# GitHub Token
export DATALAD_CREDENTIAL_GITHUB_TOKEN="{your-github-token}"

# AWS credentials
export AWS_ACCESS_KEY_ID="{access_key_id}"
export AWS_SECRET_ACCESS_KEY="{secret_access_key}"
```


