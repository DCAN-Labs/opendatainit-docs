# Step 4: Set up DataLad Repository

This guide walks through setting up DataLad using BOB's Repository as an example, including creating a sibling GitHub repository to store metadata for provenance and configuring Amazon S3 as a special remote for public data sharing. 

---

## Set Up Environment

See [Step 3.2 Before running any DataLad workflow](setup.md#32-before-running-any-datalad-workflow).


---

## Initialize DataLad Repository 

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

## Generate GitHub Sibling Repository

To create the GitHub sibling, run:

```bash
datalad create-sibling-github -d . DCAN-Labs/{REPO_NAME} --credential github
```

*DataLad specifically supports credentials through an environment variable named `DATALAD_CREDENTIAL_<CREDENTIAL-NAME>_TOKEN`, so `--credential github` used to create the GitHub sibling in corresponds to `DATALAD_CREDENTIAL_GITHUB_TOKEN` that you defined during setup [here](setup.md#32-before-running-any-datalad-workflow).*

You can confirm the creation of the sibling (named github) with the `datalad siblings` command:
```bash
$ datalad siblings
.: here(+) [git]
.: github(-) [https://github.com/DCAN-Labs/{REPO_NAME}.git (git)]
```

---

## Connect to AWS S3

### Set Environmental Variables
Once your AWS S3 bucket is generated, AWS access and secret keys will be provided to you by the Informatics Hub. **Note that these credentials are distinct from your MSI credentials and are required for using Amazon AWS as a special remote.** 

Activate your conda environment (if you haven't already) and set your AWS access and secret keys as environmental variables in order to be able to push changes to AWS:

```bash
# Set AWS credentials as environmental variables
export AWS_ACCESS_KEY_ID="<access_key_id>"
export AWS_SECRET_ACCESS_KEY="<secret_access_key>"
```

### Add Amazon S3 as Special Remote

The process for adding an Amazon S3 as a special remote is described in the DataLad Handbook - see [Walk-through: Amazon S3 as a special remote](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#). Note that the default behavior of DataLad is to name files with MD5 hashes, used by `git-annex` under the hood to manage file versioning. For accessibility, we use the flags `exporttree=yes` and `versioning=yes` to use use the original file names instead of replacing them with MD5 hashes.


<!-- First flag used in isolation will cause you to lose the direct linkage to the hash-based versioning system, overwriting and removing access to older file versions. The flag `versioning=yes` is therefore required in order to preserve prior file versions on AWS. -->

To add Amazon S3 as a special remote, use the following command:

```bash
git annex initremote aws \
    type=S3 \
    encryption=none \
    bucket={REPO_NAME} \
    datacenter=us-east-2 \
    autoenable=true \
    exporttree=yes \
    versioning=yes
```

Then configure anonymous retrieval to allow downloads from the bucket without requiring AWS credentials:

```bash
git annex enableremote aws \
    publicurl=https://{REPO_NAME}.s3.us-east-2.amazonaws.com
```

---

## Update GitHub sibling configuration

Update the dependencies for your GitHub sibling repository with the flag `--publish-depends aws`. This flag sets a publication dependency so that whenever you push your changes, the annexed contents are first pushed to the special remote and then GitHub (so that the information is updated/annexed across platforms):

```bash
datalad siblings configure \
    -d . \
    -s github \
    --publish-depends aws
```

## Publish
Push updated file contents and data provenance for versioning to S3 and Github. The first command is required when using the `exporttree=yes` flag for special remotes. Also note that you may have to enter your GitHub credentials a few times with the final command:

```bash
git annex export main --to aws
datalad push --to github
```

You should now be able to see the updated files on S3 and symlinks in Github (these are not the files, but rather symbolic links to annexed data on the S3 remote).

## Starting from Scratch

This should be avoided of course, but sometimes configuration errors with the initial setup are more quickly solved by starting from scratch. To do so, delete all of the following:

- GitHub repository (do not create a new one after deleting- this will be done automatically as part of the configuration process)
- DataLad repository on MSI/local (if you get permission denied, change permissions and then delete)
- Amazon AWS bucket contents 

**NEVER DELETE ORIGINAL SOURCE DATA STORED OUTSIDE OF THE DATALAD REPOSITORY**


