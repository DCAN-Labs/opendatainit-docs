# Conda Environment Setup

**Additional information provided for [Step 3: Set up DataLad Repository](../sop/step3-datalad.md).**

## Overview

There are specific version requirements for `datalad` and `git annex` in order to be able to set up Amazon S3 as a special remote (see [DataLad documentation](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#)). If the central CDNI-wide conda environment doesn't work, check whether the package versions meet the requirements in the DataLad documentation. If not, you will want to create your own environment. 

As of July 2026, the current package versions for the central CDNI `datalad` environment on MSI are:

**DataLad Packages**

| Name              | Version | Build        | Channel     |
| ----------------- | ------- | ------------ | ----------- |
| datalad           | 0.17.8  | pypi_0       | pypi        |
| datalad-container | 1.1.4   | pyhd8ed1ab_0 | conda-forge |
| datalad-installer | 0.3.1   | pypi_0       | pypi        |


**git-annex Package**

| Name      | Version     | Build            | Channel     |
| --------- | ----------- | ---------------- | ----------- |
| git-annex | 10.20250828 | nodep_h1234567_0 | conda-forge |


## Setting up your own conda env

See details on [CDNI BRAIN](https://cdnis-brain.readthedocs.io/vscode/#conda-environments) for how to do this, but the basic steps will be:

Note: for the name of the env, don't just use `datalad` or you might get confused with the existing CDNI environment. Choose something unique like using your x500 id, e.g. `datalad_lmoore`.

```
source /projects/standard/faird/shared/code/external/envs/miniconda3/load_miniconda3.sh
conda create --name {ENV NAME}     
conda activate {ENV NAME}

# Activate and install dependencies
source activate my_datalad_env
conda install -c conda-forge datalad
conda install -c conda-forge git-annex=*=alldep*
```

The `git-annex` install of the standard distribution above (with `git-annex=*=alldep*`) will allow you to use the `signature=v4` flag in git annex `initremote` commands, which is required for the workflow to work correctly (basically this allows you to display the files in the public repo using human-readable filenames instead of hashes).