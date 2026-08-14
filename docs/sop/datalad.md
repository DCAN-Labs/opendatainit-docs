# Initialize DataLad

This guide walks through setting up DataLad, including creating a sibling GitHub repository to store metadata for provenance and configuring Amazon S3 as a special remote for public data sharing. 

!!! warning "Always remember to initialize your environment first"
    Remember to set up your environment first if you haven't already - see [Before running any DataLad workflow](setup.md#before-running-any-datalad-workflow).

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

## Generate GitHub Sibling

Create a GitHub repository in the DCAN-Labs organization and configure it as a DataLad sibling with the following command. Replace `{REPO_NAME}` with the name of the GitHub repository. Note that the `--credential github` option tells DataLad to use the credential named `github`, which corresponds to the `DATALAD_CREDENTIAL_GITHUB_TOKEN` environment variable [defined during env setup](setup.md#before-running-any-datalad-workflow). 

```bash
datalad create-sibling-github -d . DCAN-Labs/{REPO_NAME} --credential github
```

To confirm that the github sibling was created, run `datalad siblings`, which should return something like this:

```bash
$ datalad siblings
.: here(+) [git]
.: github(-) [https://github.com/DCAN-Labs/{REPO_NAME}.git (git)]
```

---

## Add Amazon S3 as Special Remote

See [Walk-through: Amazon S3 as a special remote](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#) in the DataLad Handbook for details. The only unique aspect of this particular setup is the use of the flags `exporttree=yes` and `versioning=yes`: the default behavior of DataLad is to name files with MD5 hashes (used by `git-annex` under the hood to manage file versioning). These 2 flags allow you to display the original filenames in the public repository instead.

#### Add Amazon S3 as a special remote

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

#### Configure anonymous downloads
Configure anonymous downloads without requiring AWS credentials:
```bash
git annex enableremote aws publicurl=https://{REPO_NAME}.s3.us-east-2.amazonaws.com

# Check your AWS configuration as needed with:
git annex info aws
```

#### Update the GitHub sibling configuration

Update with `--publish-depends aws` - this sets a publication dependency so that whenever you push your changes, the annexed contents are first pushed to the special remote and then GitHub (so that the information is updated/annexed across platforms):

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

##### ⚠️ Troubleshooting

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


