# Step 3: Set up DataLad Repository

This guide walks through setting up DataLad using BOB's Repository as an example, including configuring Amazon S3 as a special remote. For additional details, see: [Walk-through: Amazon S3 as a special remote](https://handbook.datalad.org/en/latest/basics/101-139-s3.html#).


1. Activate CDNI-wide datalad conda environment: 

`source /projects/standard/faird/shared/code/external/envs/miniconda3/load_miniconda3.sh`       
`conda activate datalad`






## NOTES
- may need to provide instructions for setting up your own conda env instead since special config may be required for this unusual use case for datalad
    - point to [CBRAIN instructions](https://cdnis-brain.readthedocs.io/vscode/#conda-environments)
    - activate conda env and then create: `conda create --name <my_datalad_env>`
    - people may need to check that git-annex version is recent enough - see requirements in DataLad documentation linked above (walkthrough for Amazon S3 as special remote)









<br><br><br><br><br>

## ARCHIVE/NOTES:

**Install DataLad and git annex** - should no longer be necessary hopefully 

```
source activate my_datalad_env
conda install -c conda-forge datalad
conda install -c conda-forge git-annex=*=alldep*
```

Note that the git-annex install of the standard distribution will require that you include the signature=v4 flag in git annex initremote commands in order to work correctly. Do NOT use the MSI modules for datalad or git-annex because the versions are too old to work for this process (git-annex version 8.20201 or higher required).


**CURRENT MSI VERSIONS FOR CENTRAL DATALAD ENV:**

DataLad Packages

| Name              | Version | Build        | Channel     |
| ----------------- | ------- | ------------ | ----------- |
| datalad           | 0.17.8  | pypi_0       | pypi        |
| datalad-container | 1.1.4   | pyhd8ed1ab_0 | conda-forge |
| datalad-installer | 0.3.1   | pypi_0       | pypi        |



git-annex Package

| Name      | Version     | Build            | Channel     |
| --------- | ----------- | ---------------- | ----------- |
| git-annex | 10.20250828 | nodep_h1234567_0 | conda-forge |

