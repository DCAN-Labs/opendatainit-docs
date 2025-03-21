# Integration With OpenNeuro

The steps below are derived from the documentation for OpenNeuro Documentation [here](https://docs.openneuro.org/#openneuro-documentation) - please see this page for further details. Note that these steps do not need to be performed separately from the intitial [DataLad setup and configuration](datalad-init.md), but the OpenNeuro interface is still under development, so we recommend following those steps first to ensure that the basic setup is correct before proceeding with configuring OpenNeuro as a GitHub sibling or special remote.

## Configure credentials

- If you haven't already, create an account on [OpenNeuro](https://openneuro.org/) using your UMN email
- Generate an API key at [https://openneuro.org/keygen](https://openneuro.org/keygen) - save this somewhere private
- Run `deno run -A jsr:@openneuro/cli login to configure credentials`. This prompts you for the required configuration fields and these are saved in Deno’s local storage. Choose openneuro instance when uploading to public data repo hosted on OpenNeuro

OR specify as environment variable:

```
export OPENNEURO_API_KEY=<api_key>
deno run -A jsr:@openneuro/cli login --error-reporting true
```

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