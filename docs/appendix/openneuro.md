!!! warning "WARNING: PAGE CURRENTLY BEING UPDATED"

# Integration With OpenNeuro

The steps below are derived from the documentation for OpenNeuro Documentation [here](https://docs.openneuro.org/#openneuro-documentation) - please see this page for further details. Note that at the time this was written, the OpenNeuro interface was still under development, so it's possible that the processes outlined below have since become more automated and user-friendly.


## Configure OpenNeuro Credentials

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

----

## Add OpenNeuro as a GitHub Sibling
Setting up OpenNeuro as a special remote similar to the Amazon S3 is not necessary, instead you can push changes via git via the command below (replacing [`https://openneuro.org/datasets/ds005450`](https://openneuro.org/datasets/ds005450), which is the location of BOBSRepository on OpenNeuro, with the location of your repository). During this stage of development, we contacted the OpenNeuro team directly to create a repository for us first that we then add, but that may not be necessary in the future. In addition, there should be support for creating snapshots of sparse datasets from the web UI in the near future.

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
