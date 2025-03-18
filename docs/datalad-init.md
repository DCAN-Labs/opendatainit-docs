# Initialize & Configure DataLad Repository

This guide walks through setting up DataLad using BOB's Repository as an example, including configuring Amazon S3 as a special remote. For additional details, see: [Walk-through: Amazon S3 as a special remote](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#).


## NOTE: For Small Data Repositories Only
This SOP is designed for small repositories (e.g., <10 GB) that can be reasonably downloaded as a zip file via a web browser.

Larger neuroimaging datasets often contain hundreds to thousands of subjects, making it impractical to download the entire dataset at once. Instead, large datasets should be structured differently, employing dataset hierarchies to create [subdatasets/submodules](https://docs.datalad.org/en/stable/generated/man/datalad-subdatasets.html) for each subject folder. Large repositories also typically have their source data stored in [tier 2 storage](https://msi.umn.edu/our-resources/knowledge-base/stratus-faqs/what-tier-2-storage)

For guidance on handling large datasets, please refer to the adapted workflow in the [internal documentation](https://docs.google.com/document/d/1qEC6YwhW-kik2z1EZAlhhUgNSrgH9XlweW-avR00Yls/edit?usp=sharing).

## Initialize DataLad Repository
### Activate Conda Environment and Set Environmental Variables
Activate your conda environment:
```bash
module load conda
source activate datalad_BR
```

Set your AWS access and secret keys as environmental variables or source stored credentials if you have a `~/.aws/fcpindi.sh` file configured (see instructions [here](installation.md#store-aws-credentials-github-token-optional)):
```bash
# Set AWS credentials as environmental variables
export AWS_ACCESS_KEY_ID="<access_key_id>"
export AWS_SECRET_ACCESS_KEY="<secret_access_key>"

# OR source stored credentials
source ~/.aws/fcpindi.sh
```

*Note: if you are using Amazon AWS as a special remote, then the AWS access and secret keys will be provided to you by the Informatics Hub.*

### DataLad: Initialize Repository!
Go to your project folder, initialize datalad, and save (`datalad save` basically combines git commit and git push):
```bash
cd /path/to/your/datalad/repo
datalad create --force 
datalad save -m "example commit message"
```

Use `datalad status` command as needed to make sure local changes are tracked

## Add Amazon S3 as Special Remote
Documentation on how to add Amazon AWS as a special remote can be found in the DataLad Handbook [here](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#).

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

## Create GitHub Sibling
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

## Publish
Push updated file contents and data provenance for versioning to S3 and Github. The first command is required when using the `exporttree=yes` flag for special remotes. Also note that you may have to enter your GitHub credentials a few times with the final command:

```bash
git annex export main --to aws
datalad push --to github
```

You should now be able to see the updated files on S3 and symlinks in Github (these are not the files, but rather symbolic links to annexed data on the S3 remote).

## Starting Over
This should be avoided of course, but if you need to delete your repository and remake it due to errors in configuration that can't be resolved, remember to delete all of the following (DO NOT DELETE SOURCE DATA!):

- GitHub repo - do not create a new one after deleting: this will be done automatically as part of the configuration process
- DataLad repository on MSI/local (if you get permission denied, change permissions and then delete)
- Amazon AWS contents 

## Additional Resources
**DataLad Handbook:**   
[8.4 Walk-through: Amazon S3 as a special remote](https://handbook.datalad.org/en/latest/basics/101-139-s3.html)  
[8.4.6 Advanced Examples](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#advanced-examples)    
[Basic Principles: Data Nesting](https://3.basecamp.com/5032058/buckets/32547817/todos/7776568105)