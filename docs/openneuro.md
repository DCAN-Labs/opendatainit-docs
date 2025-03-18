# Step 4: Integration With OpenNeuro

BOBSRepository on OpenNeuro: https://openneuro.org/datasets/ds005450

## Configure credentials

- Generate API here after logging into your account
- Run `deno run -A jsr:@openneuro/cli login to configure credentials`. This prompts you for the required configuration fields and these are saved in Deno’s local storage. Choose openneuro instance when uploading to public data repo hosted on OpenNeuro

OR specify as environment variable:

```
export OPENNEURO_API_KEY=<api_key>
deno run -A jsr:@openneuro/cli login --error-reporting true
```


## Push Changes to OpenNeuro Repository

Setting up OpenNeuro as a special remote is not necessary, instead you can push changes via git:

```bash
$ datalad siblings add --url https://openneuro.org/git/0/ds005450
[INFO   ] Could not annex-enable openneuro.org:   Remote openneuro.org not usable by git-annex; setting annex-ignore
  https://openneuro.org/git/0/ds005450/config download failed: Not Found
  Remote openneuro.org not usable by git-annex; setting annex-ignore
  https://openneuro.org/git/0/ds005450/config download failed: Not Found
enableremote: 1 failed
 
.: openneuro.org(-) [https://openneuro.org/git/0/ds005450 (git)]

$ datalad push --to openneuro.org --data nothing
```