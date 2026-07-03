# Local Installation & Configuration


## Install OpenNeuro CLI

- Install deno: `conda install conda-forge::deno`
- Run `deno run -A jsr:@openneuro/cli --help` - should see usage if it’s working

## Configure Git Credentials 
Make sure your [git credentials are configured](https://handbook.datalad.org/en/latest/intro/installation.html#initial-configuration). This will be required when creating the sibling GitHub repository:

```bash
cd ~
git config --global --add user.name "Bob McBobFace"
git config --global --add user.email bob@example.com
```

Also make sure to run the following command in order to automatically use “main” instead of “master” for the main branch of your new GitHub repository that will be created:

```
git config --global init.defaultBranch main
```

## Store AWS Credentials & GitHub Token (Optional)

Whenever you work with your DataLad repository, you need to first activate the conda environment and then set your AWS access and secret keys as environmental variables in order to be able to push changes to AWS:
```bash
module load conda
source activate datalad_BR
export AWS_ACCESS_KEY_ID="<access_key_id>"
export AWS_SECRET_ACCESS_KEY="<secret_access_key>"
```

Alternatively, you may store the secret keys in `.aws/fcpindi.sh` and simply run the following in place of the 2 export lines above:
```bash
source ~/.aws/fcpindi.sh
```

This file should include the following variables, used by DataLad to [interact with AWS](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#prerequisites) and GitHub: 

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `DATALAD_CREDENTIAL_GH_TOKEN`