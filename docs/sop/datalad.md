# Step 3: Set up DataLad Repository

This guide walks through setting up DataLad using BOB's Repository as an example, including creating a sibling GitHub repository to store metadata for provenance and configuring Amazon S3 as a special remote for public data sharing. 

---

## 3.1: Initial Setup & Conda Environment

### Configure Git Credentials 
Make sure your [git credentials are configured](https://handbook.datalad.org/en/latest/intro/installation.html#initial-configuration). This will be required when creating the sibling GitHub repository. **THIS ONLY NEEDS TO BE DONE ONCE.**

```bash
cd ~
git config --global --add user.name "Bob McBobFace"
git config --global --add user.email bob@example.com
```

### Activate Conda Environment
Activate the CDNI-wide datalad conda environment: 

```bash
source /projects/standard/faird/shared/code/external/envs/miniconda3/load_miniconda3.sh
conda activate datalad
```

!!! warning "Warning: Conda Environments"
    If you run into potential issues with the conda environment at any point, such as errors about incorrect package versions or commands not working as expected, see [Troubleshooting > Conda Environment Setup](../appendix/troubleshooting.md#conda-environment-setup).

---

## 3.2: Initialize DataLad

### Initialize DataLad Repository 

Go to your project folder, initialize datalad, and save:
```bash
cd /path/to/your/datalad/repo
datalad create --force
datalad save -m "initial commit"
```

<!-- NOTE: for Julia repo, time for single zip file (~50GB) was ~4 min for this step -->

- `--force` is necessary for non-empty folders
- `datalad save` basically combines `git commit` and `git push` commands

Use `datalad status` command as needed to make sure local changes are tracked

### Create GitHub Sibling
Next, DataLad creates an empty dataset repository on GitHub. The flag `--publish-depends SIBLINGNAME` sets a publication dependency so that whenever you push your changes, the annexed contents are first pushed to the special remote and then GitHub: 

```bash
datalad create-sibling-github -d . DCAN-Labs/bobsrepository /
--publish-depends aws --credential <GitHub username>
```

Confirm the creation of the sibling (named github) with datalad siblings - example from handbook:
```bash
$ datalad siblings
.: here(+) [git]
.: aws(+) [git]
.: github(-) [https://github.com/DCAN-Labs/bobsrepository.git (git)]
```

## 3.3: Connect to AWS S3 & Publish

### Set Environmental Variables
Once your AWS S3 bucket is generated, AWS access and secret keys will be provided to you by the Informatics Hub. **Note that these credentials are distinct from your MSI credentials and are required for using Amazon AWS as a special remote.** 

After activating the conda environment, set your AWS access and secret keys as environmental variables in order to be able to push changes to AWS:

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
git annex initremote aws type=S3 encryption=none bucket=bobsrepository /
autoenable=true signature=v4 datacenter=us-east-2 public=yes exporttree=yes versioning=yes
```

Set bucket URL for git-annex to be able to download files from the bucket without requiring your AWS credentials:
```bash
git annex enableremote aws publicurl="https://bobsrepository.s3.amazonaws.com”
```

### Publish
Push updated file contents and data provenance for versioning to S3 and Github. The first command is required when using the `exporttree=yes` flag for special remotes. Also note that you may have to enter your GitHub credentials a few times with the final command:

```bash
git annex export main --to aws
datalad push --to github
```

You should now be able to see the updated files on S3 and symlinks in Github (these are not the files, but rather symbolic links to annexed data on the S3 remote).




