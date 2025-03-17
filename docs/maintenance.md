# Repository Maintenance

## First Steps
When working with your DataLad repository, always start by activating your conda environment and setting the necessary environment variables:

```bash
module load conda
source activate datalad_BR
export AWS_ACCESS_KEY_ID="<access_key_id>"
export AWS_SECRET_ACCESS_KEY="<secret_access_key>"
```

## Updating repository files/contents
See the [Modify Content](https://handbook.datalad.org/en/latest/basics/101-103-modify.html#modify-content) section of the DataLad Handbook. 

Files that are annexed for version control are write-protected to ensure file integrity by default. Instead of forcefully changing the permissions of the file in order to edit it, use datalad unlock, otherwise you may jeopardize the version control and file integrity. For example: 
```bash
datalad unlock sub-xxxx_ses-xmo_space-INFANTMNIacpc_desc-aseg_dseg.nii.gz
```

If you have a zip file included for quick download, you’ll need to recreate the zip file with the following commands so that it contains the most current data for quick download:
```bash
datalad unlock *
zip -r bobsrepository.zip dataset_description.json participants.tsv sub-*
```

To save and push your changes, run:
```bash
datalad save -m "Description of changes"
git annex export main --to aws
datalad push --to github
```
This will automatically lock the files again.

## Accessing previous file versions

List versions using AWS CLI:
```bash
aws s3api list-object-versions --bucket mybucket --prefix path/to/file
```

And download a specific version via:
```bash
aws s3api get-object --bucket mybucket --key path/to/file --version-id version_id local_file
```