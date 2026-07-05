# MIDB Open Data Initiative

Welcome to the documentation for creating and publishing datasets through the Masonic Institute for the Developing Brain Open Data Initiative (**MIDB ODI**)! The MIDB ODI integrates [Amazon S3](https://aws.amazon.com/s3/) for storage, DataLad for version control, and AWS and OpenNeuro for public data access. Data are hosted through the AWS [Open Data Sponsorship Program](https://aws.amazon.com/opendata/open-data-sponsorship-program/), supporting public distribution, management, and tracking of datasets.

**This guide provides internal SOPs for MIDB users who wish to share their dataset via the MIDB ODI, including:**

 - Setting up a DataLad repository for versioning and data provenance
 - Publishing dataset for public access via AWS (and OpenNeuro as well if desired)

!!! warning "WARNING: Scope & Limitations"
    **This workflow currently supports small datasets only** (i.e. that can be downloaded as one or more zip files via a web browser). Support for larger datasets is planned using DataLad [subdatasets](https://docs.datalad.org/en/stable/generated/man/datalad-subdatasets.html) organized by subject folder, with source data stored in [tier 2 storage](https://msi.umn.edu/our-resources/knowledge-base/stratus-faqs/what-tier-2-storage). 




<!-- ## Adding A New Repository: Internal SOPs -->
<!-- Using the [BOBS Repository](https://bobsrepository.readthedocs.io) as an example use case, it covers:

 - Setting up DataLad repository for versioning and tracking of data provenance        
 - Making the data repository publicly available via **Amazon AWS** and **OpenNeuro**         -->

<!-- See the [Checklist](helper-files/checklist.md) provided for help tracking the required action items. -->


<!-- For guidance on handling large datasets, please refer to the adapted workflow in the [internal documentation](https://docs.google.com/document/d/1qEC6YwhW-kik2z1EZAlhhUgNSrgH9XlweW-avR00Yls/edit?usp=sharing). -->


