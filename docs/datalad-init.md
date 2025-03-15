# Initializing DataLad Repository

**The following uses bobsrepository as an example. Replace bobsrepository with the name of your repository.**

### Activate Conda Environment and Set Environmental Variables
Activate your conda environment and set your AWS access and secret keys as environmental variables:
```bash
module load conda
source activate datalad_BR
export AWS_ACCESS_KEY_ID="<access_key_id>"
export AWS_SECRET_ACCESS_KEY="<secret_access_key>"
```

### Initialize DataLad repo
```bash
cd /path/to/your/datalad/repo
datalad create --force 
datalad save -m "added subset of data"
```

### Add Amazon S3 as Special Remote
The flags `exporttree=yes` and `versioning=yes` use the original file names instead of replacing them with MD5 hashes. Because MD5 hashes are used for version control, the first flag used in isolation will cause you to lose the direct linkage to the hash-based versioning system, overwriting and removing access to older file versions. The flag `versioning=yes` is therefore required in order to preserve prior file versions on AWS.

```bash
git annex initremote aws type=S3 encryption=none bucket=bobsrepository /
autoenable=true signature=v4 datacenter=us-east-2 public=yes exporttree=yes versioning=yes
```

Set bucket URL for git-annex to be able to download files from the bucket without requiring your AWS credentials:
```bash
git annex enableremote aws publicurl="https://bobsrepository.s3.amazonaws.com”
```

### Create GitHub Sibling
Next, DataLad creates an empty dataset repository on GitHub. The flag `--publish-depends SIBLINGNAME` sets a publication dependency so that whenever you push your changes, the annexed contents are first pushed to the special remote and then GitHub: 

```bash
datalad create-sibling-github -d . DCAN-Labs/bobsrepository /
--publish-depends aws --credential LuciMoore
```

Confirm the creation of the sibling (named github) with datalad siblings - example from handbook:
```bash
$ datalad siblings
.: here(+) [git]
.: aws(+) [git]
.: github(-) [https://github.com/DCAN-Labs/bobsrepository.git (git)]
```

### Publish
Push updated file contents and data provenance for versioning to S3 and Github. The first command is required when using the exporttree=yes for special remotes. Also note that you may have to enter your GitHub credentials a few times with the final command:

```bash
git annex export main --to aws
datalad push --to github
```

### Starting Over
This should be avoided of course, but if you need to delete your repository and remake it due to errors in configuration that can't be resolved, remember to delete all of the following (DO NOT DELETE SOURCE DATA!):

- GitHub repo - do not create a new one after deleting: this will be done automatically as part of the configuration process
- DataLad repository on MSI/local (if you get permission denied, change permissions and then delete)
- Amazon AWS contents 
