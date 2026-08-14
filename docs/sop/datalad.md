# Initialize DataLad

This guide walks through the steps to convert your dataset to a DataLad repository (which only need to be completed once). The workflow uses (1) GitHub to host the Git repository and DataLad/git-annex metadata for provenance and (2) Amazon S3 as a special remote for storing and publicly distributing the actual annexed file content.

!!! warning "Always remember to initialize your environment first"
    Remember to set up your environment first- see [Before running any DataLad workflow](setup.md#before-running-any-datalad-workflow).

## Initial Setup
### 1. Initialize DataLad Repository 

Navigate to your project directory and initialize it as a DataLad dataset, replacing `{REPO_NAME}` with the name of your project folder:

```bash
cd /path/to/{REPO_NAME}
datalad create --force # required if folder is non-empty
datalad save -m "initial commit" 

# Check for unsaved local changes any time with:
datalad status
```

Note that the `datalad save` command records the current state of the dataset in a new commit, but does not push those changes to GitHub or S3.

### 2. Create the GitHub Sibling

Create a GitHub repository in the DCAN-Labs organization and configure it as a DataLad sibling (replacing `{REPO_NAME}` with the name your repository):

```bash
datalad create-sibling-github -d . DCAN-Labs/{REPO_NAME} --credential github
```

The `--credential github` option tells DataLad to use the credential named `github`. Its token is provided by the `DATALAD_CREDENTIAL_GITHUB_TOKEN` environment variable defined during environment setup ([see details](setup.md#before-running-any-datalad-workflow)).

Verify that the Github sibling was created with `datalad siblings`:

```bash
$ datalad siblings
.: here(+) [git]
.: github(-) [https://github.com/DCAN-Labs/{REPO_NAME}.git (git)]
```

### 3. Configure the S3 Special Remote

Amazon S3 is used as a git-annex special remote to store and publicly distribute annexed file content. See the DataLad Handbook's [Amazon S3 as a special remote](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#) documentation for details. The flags `exporttree=yes` and `versioning=yes` are used to export using the dataset's filenames and directory structure rather than git-annex's internal object layout so that the dataset contents are displayed as human-readable filenames on AWS instead of, for example, MD5 hashes (used by `git-annex` under the hood to manage file versioning).

```bash
git annex initremote aws \
    type=S3 \
    encryption=none \
    bucket={REPO_NAME} \
    datacenter=us-east-2 \
    autoenable=true \
    exporttree=yes \
    versioning=yes

# Configure anonymous downloads without requiring AWS credentials:
git annex enableremote aws publicurl=https://{REPO_NAME}.s3.us-east-2.amazonaws.com

# Check your AWS configuration as needed with:
git annex info aws
```

<!-- #### Update the GitHub sibling configuration -->

### 4. Configure Publication Dependency

Configure the GitHub sibling to depend on the `aws` special remote as follows. This sets a publication dependency so that whenever you push your changes, the annexed contents are first pushed to the special remote and then GitHub (so that the information is updated/annexed across platforms):

```bash
datalad siblings configure -d . -s github --publish-depends aws
```

---

## Publish

Push updated file contents and data provenance for versioning to S3 and Github. The first command is required when using the `exporttree=yes` flag for special remotes. Also note that you may have to enter your GitHub credentials a few times with the final command:

```bash
git annex export main --to aws
datalad push --to github
```
You should now be able to see the updated files on S3 and symlinks in Github (these are not the files, but rather symbolic links to annexed data on the S3 remote).

---

## ⚠️ Troubleshooting

If you get an error about file size limits, try adding `partsize=1GiB` to the configuration:

```bash
git annex enableremote aws partsize=1GiB
```

If you get an error with datalad push, then try this instead:

```bash
git push github main
git push github git-annex
```

---

## Starting from Scratch

This should be avoided of course, but sometimes configuration errors with the initial setup are more quickly solved by starting from scratch. To do so, delete all of the following:

- GitHub repository (do not create a new one after deleting- this will be done automatically as part of the configuration process)
- DataLad repository on MSI/local (if you get permission denied, change permissions and then delete)
- Amazon AWS bucket contents 

**NEVER DELETE ORIGINAL SOURCE DATA STORED OUTSIDE OF THE DATALAD REPOSITORY**


