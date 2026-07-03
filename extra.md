    <a class="download-link" href="https://infant_3T_7T_precision_imaging_datalad.s3.us-east-2.amazonaws.com/V1.0.zip" download>Download Entire Repository</a>


<a class="download-link" href="https://infant_3T_7T_precision_imaging_datalad.s3.us-east-2.amazonaws.com/V1.0.zip" download>Download Entire Repository</a>



 dataPB015.zip
dataPB016.zip
dataPB017.zip
dataPB020.zip
dataPB021.zip
dataPB022.zip



 
 For example, in the BOBS Repository, there are the files `index.html` and `V1.0.zip`: 

```
bobsrepository/
|__ sub-<LABEL>/
|   |__ ses-<AGE>mo/
|       |__ anat/
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-T1w.nii.gz
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-T1w.json
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-T2w.nii.gz
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-T2w.json
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-aseg_dseg.nii.gz
|           |__sub-<LABEL>_ses-<AGE>_space-INFANTMNIacpc_desc-aseg_dseg.json
|
|__ phenotype/
|   |__ sessions.json
|   |__ sessions.tsv
|
|__ dataset_description.json
|__ dseg.tsv
|__ README.md
|__ index.html #.bigsignore
|__ V1.0.zip #.bigsignore
``` -->

<!-- When your folder is fully set up, run BIDS validation as a final check. Also remember to run BIDS validation after adding any additional files needed (e.g. `index.html` and a zip file - see [Amazon AWS Configuration](#amazon-aws-configuration))
```bash
module load conda
source activate datalad_BR
deno run -A jsr:@bids/validator <dataset path> > /path/to/denoresults.txt
```
