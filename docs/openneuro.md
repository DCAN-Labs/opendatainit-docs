# Integration With OpenNeuro

BOBSRepository on OpenNeuro: https://openneuro.org/datasets/ds005450

## Configure credentials

- Generate API here after logging into your account
- Run `deno run -A jsr:@openneuro/cli login to configure credentials`. This prompts you for the required configuration fields and these are saved in Deno’s local storage. Choose openneuro instance when uploading to public data repo hosted on OpenNeuro

OR specify as environment variable:

```
export OPENNEURO_API_KEY=<api_key>
deno run -A jsr:@openneuro/cli login --error-reporting true
```

## Add OpenNeuro as a GitHub Sibling
Setting up OpenNeuro as a special remote is not necessary, instead you can push changes via git:

```bash
$ datalad siblings add --url https://openneuro.org/git/0/ds005450
[INFO   ] Could not annex-enable openneuro.org:   
  Remote openneuro.org not usable by git-annex; setting annex-ignore
  https://openneuro.org/git/0/ds005450/config download failed: Not Found
 
.: openneuro.org(-) [https://openneuro.org/git/0/ds005450 (git)]
```
Note that you may see the messages like the ones displayed above. The first (`Remote openneuro.org not usable by git-annex; setting annex-ignore`) simply indicates that the GitHub repository does not actually contain the annexed files themselves, but rather symlinks to the data files stored in local DataLad repository - this is expected behavior. The second ()`https://openneuro.org/git/0/ds005450/config download failed: Not Found`) indicates that the remote repository is lacking a config file, which is okay. As long as there are no error messages, then it should have worked.

## Push Changes to OpenNeuro Repository
Finally, to push changes to OpenNeuro:
```bash
$ datalad push --to openneuro.org --data nothing
```