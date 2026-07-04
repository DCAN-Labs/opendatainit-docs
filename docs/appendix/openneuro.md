# Integration With OpenNeuro

The steps below are derived from the documentation for OpenNeuro Documentation [here](https://docs.openneuro.org/#openneuro-documentation) - please see this page for further details. Note that at the time this was written, the OpenNeuro interface was still under development, so details below may need to be updated.

## Step 1: Configure OpenNeuro Credentials

### Create OpenNeuro account and generate API
- If you haven't already, create an account on [OpenNeuro](https://openneuro.org/) using your UMN email
- Generate an API key at [https://openneuro.org/keygen](https://openneuro.org/keygen) - save this somewhere private

### Install OpenNeuro CLI in your datalad conda environment
- Install deno then the following help command to test that it's working (should see usage printed out if so)

```
conda install conda-forge::deno
deno run -A jsr:@openneuro/cli --help
```
### Configure OpenNeuro credentials
Configure credentials via one of the following methods:

**(1)** Run the following on the command line, which will prompt you to enter the required configuration fields that are then saved in Deno's local storage. If asked, choose "openneuro" instance when uploading to public data repo hosted on OpenNeuro.
```
deno run -A jsr:@openneuro/cli login
```
**OR (2)** set as environment variable whenever working in your repo:
```
export OPENNEURO_API_KEY=<api_key>
deno run -A jsr:@openneuro/cli login --error-reporting true
```

---

## Step 2: OpenNeuro Compatibility Configuration
Proper configuration is required in order to connect your DataLad repository to OpenNeuro is described in their documentation on the page [Git access to OpenNeuro datasets](https://docs.openneuro.org/git.html). In our case, you simply need to add a `.gitattributes` file to your repository, which is required for `git-annex` to automate annexing the correct files when using `git add` or `datalad save`.

Use the recommended configuration provided in their documentation:

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
!!! note "Additional Information"    
    The information below is not required for you to complete setup, but helpful to review so you can understand the process. 

    - `* annex.backend=SHA256E`: by default, `git-annex` uses MD5E as the backend for S3. However, other backends (SHA256E, SHA1E) also work for AWS, so this shouldn't cause you any issues
    - `annex.largefiles`: OpenNeuro requires that certain files, particularly large files, be annexed (vs. kept as regular git files). Since we have already converted your repository to a DataLad repository, this step will already be complete! In addition, certain files are required to be kept as regular git files (e.g. `.bidsignore`). By default, DataLad does not annex these types of files, so this shouldn't be an issue for you either.
    - `annex.largefiles` Configuration Details
        - `annex.largefiles=nothing`: File is always stored in Git, never annexed *(e.g. `README`, `dataset_description.json`, `.bidsignore`)*
        - `annex.largefiles.largerthan=1mb`: Files >1MB go into annex, smaller ones stay in Git *(e.g., all `.json` files smaller than 1mb)*
        - `annex.largefiles=anything`: File is always stored in annex, no matter the size *(e.g., `phenotype/*.tsv` files)*

OpenNeuro validates the size of regular git (non-annexed) files and a subset of bids-validation before accepting a `git push`. **Datasets will not be published to OpenNeuro without fully passing BIDS validation.**
 
---

## Step 3: Add OpenNeuro as a GitHub Sibling
Setting up OpenNeuro as a special remote similar to the Amazon S3 is not necessary, instead you can push changes via git via the command below (replacing [`https://openneuro.org/datasets/ds005450`](https://openneuro.org/datasets/ds005450), which is the location of BOBSRepository on OpenNeuro, with the location of your repository). During this stage of development, we contacted the OpenNeuro team directly to create a repository for us first that we then add, but that may not be necessary in the future. In addition, there should be support for creating snapshots of sparse datasets from the web UI in the near future.

```bash
$ datalad siblings add --url https://openneuro.org/git/0/ds005450
[INFO   ] Could not annex-enable openneuro.org:   
  Remote openneuro.org not usable by git-annex; setting annex-ignore
  https://openneuro.org/git/0/ds005450/config download failed: Not Found
 
.: openneuro.org(-) [https://openneuro.org/git/0/ds005450 (git)]
```
Note that you may see the messages like the ones displayed above. The first (`Remote openneuro.org not usable by git-annex; setting annex-ignore`) simply indicates that the GitHub repository does not actually contain the annexed files themselves, but rather symlinks to the data files stored in local DataLad repository - this is expected behavior. The second (`https://openneuro.org/git/0/ds005450/config download failed: Not Found`) indicates that the remote repository is lacking a config file, which is okay. As long as there are no error messages, then it should have worked.

---

## Step 4: Push Changes to OpenNeuro Repository
Finally, to push changes to OpenNeuro:
```bash
$ datalad push --to openneuro.org --data nothing
```
