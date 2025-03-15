# Step 1: Installation

## Create Conda Environment
There currently isn’t a lab-wide datalad environment set up on MSI with the correct dependencies for the steps below. Please create your own conda environment (also refer to instructions [here](https://cdnis-brain.readthedocs.io/vscode/#conda-environments) if needed - also note that you may need to first load conda module):

Check for available env names and make sure you choose something unique (e.g. for bobsrepository, my conda env name is datalad_BR):
```
module load conda
conda info –-envs
conda create --name <my_datalad_env>
```

## Install DataLad and git annex
```
source activate my_datalad_env
conda install -c conda-forge datalad
conda install -c conda-forge git-annex=*=alldep*
```

Note that the git-annex install of the standard distribution will require that you include the signature=v4 flag in git annex initremote commands in order to work correctly. Do NOT use the MSI modules for datalad or git-annex because the versions are too old to work for this process (git-annex version 8.20201 or higher required).

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
