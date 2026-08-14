# Prepare Source Data

**Ensure that your data is prepped, organized, and ready for public sharing.**


## BIDS Formatting

**Ensure that dataset adheres to Brain Imaging Data Structure ([BIDS](https://bids-specification.readthedocs.io/en/stable/)) standard.** This is standard practice in our group, so you likely don't need to do anything here if you are already familiar with BIDS. If in doubt, use the standard [BIDS Validator](https://bids-standard.github.io/bids-validator/) or other utility and fix all `ERRORS` (`WARNINGS` are optional/suggestions for best practice, so can be safely ignored if not applicable to your data).

---

## De-identification & Permission to Share

!!! danger "Potentially high-effort and/or time-consuming item"
    This step can be complex as the rules vary by dataset, institution, IRB protocol, etc.

**Consult with stakeholders to ensure that your data can be shared publicly without violating HIPAA or any data use agreements and update data as needed.** Updates may include, for example, removing identifiable metadata (e.g. with DICAT) and/or defacing MRI images. See [CDNI Brain](https://cdnis-brain.readthedocs.io/deidentification/#de-identification-of-mri-image-data) documentation for guidance on defacing and other de-identification methods.
