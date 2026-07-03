# EXTRA INFO TO POTENTIALLY ADD (copied from older RTDs version)

## Initialize & Configure DataLad Repository

NOTE: For Small Data Repositories Only
This SOP is designed for small repositories (e.g., <10 GB) that can be reasonably downloaded as a zip file via a web browser.

Larger neuroimaging datasets often contain hundreds to thousands of subjects, making it impractical to download the entire dataset at once. Instead, large datasets should be structured differently, employing dataset hierarchies to create [subdatasets/submodules](https://docs.datalad.org/en/stable/generated/man/datalad-subdatasets.html) for each subject folder. Large repositories also typically have their source data stored in [tier 2 storage](https://msi.umn.edu/our-resources/knowledge-base/stratus-faqs/what-tier-2-storage)

For guidance on handling large datasets, please refer to the adapted workflow in the [internal documentation](https://docs.google.com/document/d/1qEC6YwhW-kik2z1EZAlhhUgNSrgH9XlweW-avR00Yls/edit?usp=sharing).
