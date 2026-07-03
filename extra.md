

When your folder is fully set up, run BIDS validation as a final check. Also remember to run BIDS validation after adding any additional files needed (e.g. `index.html` and a zip file - see [Amazon AWS Configuration](#amazon-aws-configuration))
```bash
module load conda
source activate datalad_BR
deno run -A jsr:@bids/validator <dataset path> > /path/to/denoresults.txt
```
