# Prepare AWS Submission

Below is a step-by-step guide for preparing for submission of a new repository to AWS, adapted from the [AWS Open Data Registry README](https://github.com/awslabs/open-data-registry). Feel free to review the source documentation for more information, including the short high-level [video tutorial](https://youtu.be/5nocWdjN1DA) provided.

---

## Sync forked repository

You will be adding your dataset repo information via the DCAN-Labs fork of the main `open-data-registry` - go to [DCAN-Labs/open-data-registry](https://github.com/DCAN-Labs/open-data-registry) and click "Sync fork" to update. 

## Add YAML file for your dataset

To add information about your dataset, you will create a new YAML file under `datasets/`, which will be used to generate the summary page for your repository on AWS - e.g. the page for the [BOBs Repository](https://registry.opendata.aws/bobsrepository/) is generated from [bobsrepository.yaml](https://github.com/DCAN-Labs/open-data-registry/blob/main/datasets/bobsrepository.yaml).

**Tips/Guidance:**

- Use this [template YAML](https://github.com/DCAN-Labs/opendatainit-docs/blob/main/resources/template-yaml.yaml), which contains a reduced set of key fields as well as pre-filled fields for your convenience (see the [AWS Open Data Registry README](https://github.com/awslabs/open-data-registry#how-are-datasets-added-to-the-registry) for a full list of required and optional fields and descriptions)
- Rename the file with your exact repository name (`{REPO_NAME}.yaml`)
- Update the empty fields with information specific to your dataset - see the existing YAML files for MIDB ODI data repos for examples:
      - [bobsrepository.yaml](https://github.com/DCAN-Labs/open-data-registry/blob/main/datasets/bobsrepository.yaml)
      - [infant-3t-7t-precision-mri.yaml](https://github.com/DCAN-Labs/open-data-registry/blob/main/datasets/infant-3t-7t-precision-mri.yaml)
- **`DataAtWork > Tutorials`**: Point to a tutorial, tool, application, or publication that uses the data. If you are unsure, simply link to documentation describing the dataset structure, which should be provided for users regardless (e.g., a README, ReadTheDocs page, or an index.html file)
- **`Resources > Description > Explore`:** make sure to replace `{REPO_NAME}` with the actual repository name 
- Use valid YAML formatting, such as wrapping text containing [special characters](https://stackoverflow.com/a/22235064) in quotes (use online tools such as [https://jsonformatter.org/yaml-validator](https://jsonformatter.org/yaml-validator) to validate as needed)

---

## Submit Pull Request

**Submit PR and resolve any CI errors.** Once you finish your YAML file and add it to the DCAN-Labs repository (under `datasets/`), you can proceed to submit your PR. CI (continuous integration) checks will run and may show errors if there are issues with your YAML formatting (e.g. missing required fields or incorrect YAML formatting). Address these errors so that the PR can be merged after review by the Amazon team.
