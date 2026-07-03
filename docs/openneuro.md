# Integration With OpenNeuro



## NOTES

 as well, as datasets will not be published to OpenNeuro without fully passing BIDS validation. Our datasets are generally BIDS valid, and you may end up adding more files to your repository as part of the process of submitting to the MIDB ODI, so feel free to skip this step for now if you are already familiar with BIDS. 

Otherwise, we recommend running BIDS validation (e.g. the standard [BIDS Validator](https://bids-standard.github.io/bids-validator/)):

- `ERRORS` must be fixed
- `WARNINGS` are optional/suggestions for best practice, so can be safely ignored if not applicable to your data (and/or listed as a future continuous improvement item for your dataset)


The steps below are derived from the documentation for OpenNeuro Documentation [here](https://docs.openneuro.org/#openneuro-documentation) - please see this page for further details. Note that these steps do not need to be performed separately from the intitial [DataLad setup and configuration](datalad-init.md), but the OpenNeuro interface is still under development, so we recommend following those steps first to ensure that the basic setup is correct before proceeding with configuring OpenNeuro as a GitHub sibling or special remote.

## Configure credentials

- If you haven't already, create an account on [OpenNeuro](https://openneuro.org/) using your UMN email
- Generate an API key at [https://openneuro.org/keygen](https://openneuro.org/keygen) - save this somewhere private
- Run `deno run -A jsr:@openneuro/cli login` to configure credentials. This prompts you for the required configuration fields and these are saved in Deno’s local storage. Choose openneuro instance when uploading to public data repo hosted on OpenNeuro

OR specify as environment variable:

```
export OPENNEURO_API_KEY=<api_key>
deno run -A jsr:@openneuro/cli login --error-reporting true
```

## Install OpenNeuro CLI in your Conda Env

- Install deno: `conda install conda-forge::deno`
- Run `deno run -A jsr:@openneuro/cli --help` - should see usage if it’s working

## Add OpenNeuro as a GitHub Sibling
Setting up OpenNeuro as a special remote is not necessary, instead you can push changes via git via the command below (replacing [`https://openneuro.org/datasets/ds005450`](https://openneuro.org/datasets/ds005450), which is the location of BOBSRepository on OpenNeuro, with the location of your repository). During this stage of development, we contacted the OpenNeuro team directly to create a repository for us first that we then add, but that may not be necessary in the future. In addition, there should be support for creating snapshots of sparse datasets from the web UI in the near future.

```bash
$ datalad siblings add --url https://openneuro.org/git/0/ds005450
[INFO   ] Could not annex-enable openneuro.org:   
  Remote openneuro.org not usable by git-annex; setting annex-ignore
  https://openneuro.org/git/0/ds005450/config download failed: Not Found
 
.: openneuro.org(-) [https://openneuro.org/git/0/ds005450 (git)]
```
Note that you may see the messages like the ones displayed above. The first (`Remote openneuro.org not usable by git-annex; setting annex-ignore`) simply indicates that the GitHub repository does not actually contain the annexed files themselves, but rather symlinks to the data files stored in local DataLad repository - this is expected behavior. The second (`https://openneuro.org/git/0/ds005450/config download failed: Not Found`) indicates that the remote repository is lacking a config file, which is okay. As long as there are no error messages, then it should have worked.

## Push Changes to OpenNeuro Repository
Finally, to push changes to OpenNeuro:
```bash
$ datalad push --to openneuro.org --data nothing
```
<br><br><br><br><br><br><br><br><br>


## OTHER


## OpenNeuro Compatibility Configuration
The `.gitattributes` file needs to be properly set up mostly for OpenNeuro compatibility - see the section of their website on [Repository Conventions](https://docs.openneuro.org/git.html#repository-conventions):

> A dataset must always be present in the root level of the repository.

> OpenNeuro validates the size of regular git (non-annexed) files and a subset of bids-validation before accepting a git push. It is important to annex any large files in any commits before pushing. `.bidsignore` must always be a regular file. Some features are only available for regular files (such as diffing) and textual data is generally best kept as regular git objects.

> A recommended .gitattributes configuration for `git-annex` to automate annexing the correct files when using `git add` or `datalad save`
```
* annex.backend=SHA256E
**/.git* annex.largefiles=nothing
*.bval annex.largefiles=nothing
*.bvec annex.largefiles=nothing
*.json annex.largefiles=largerthan=1mb
phenotype/*.tsv annex.largefiles=anything
*.tsv annex.largefiles=largerthan=1mb
dataset_description.json annex.largefiles=nothing
.bidsignore annex.largefiles=nothing
CHANGES annex.largefiles=nothing
README* annex.largefiles=nothing
LICENSE annex.largefiles=nothing
```

#### Annex Backend (SHA256E vs MD5E)
OpenNeuro requires that you use SHA256E for the annex backend. `git-annex` assigns MD5E by default for S3, but other backends (SHA256E, SHA1E) also work for AWS, so you will need to specify this in the `.gitattributes` file with `* annex.backend=SHA256E` as shown above.

#### Comparison of `annex.largefiles` Rules    
Depending on the file, OpenNeuro requires or recommends that files be git-annex files vs regular git files. This is specified in `.gitattributes` by `annex.largefiles` as follows:
 
**Convention:** `annex.largefiles=nothing`      
**Meaning:** File is always stored in Git, never annexed        
**Examples:** `README`, `dataset_description.json`, `.bidsignore`

**Convention:** `annex.largefiles.largerthan=1mb`      
**Meaning:** Files >1MB go into annex, smaller ones stay in Git.        
**Examples:** All `.json` files smaller than 1mb

**Convention:** `annex.largefiles=anything`      
**Meaning:** File is always stored in annex, no matter the size.        
**Examples:** `phenotype/*.tsv` files