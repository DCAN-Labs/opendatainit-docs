# MIDB Open Data Initiative

Welcome to the Docs site for setting up a repository via the Masonic Institute for the Developing Brain (MIDB) Open Data Initiative! This initiative links S3 storage, DataLad for version control, and Amazon AWS and OpenNeuro platforms for public access. Data are hosted via the Amazon Web Services (AWS) [Open Data Sponsorship Program](https://aws.amazon.com/opendata/open-data-sponsorship-program/). The Amazon Simple Storage Service, or simply [Amazon S3](https://aws.amazon.com/s3/), allows data storage for public distribution, management, and tracking. 

---

## Adding A New Repository: Internal SOPs

This documentation is provided to guide MIDB users in setting up an open data repository via MIDB. Using the [BOBS Repository](https://bobsrepository.readthedocs.io) as an example use case, it covers:

 - Setting up DataLad repository for versioning and tracking of data provenance        
 - Making the data repository publicly available via **Amazon AWS** and **OpenNeuro**        

<!-- See the [Checklist](helper-files/checklist.md) provided for help tracking the required action items. -->

---

## Scope & Limitations
!!! warning "WARNING:  This workflow is currently intended for small datasets only"

The current workflows outlined are intended only for smaller repositories that can be reasonably downloaded as a single or series of zip files via a web browser.

Larger neuroimaging datasets often contain hundreds to thousands of subjects, making it impractical to download the entire dataset at once. Instead, large datasets should be structured differently, employing dataset hierarchies to create [subdatasets/submodules](https://docs.datalad.org/en/stable/generated/man/datalad-subdatasets.html) for each subject folder. Large repositories also typically have their source data stored in [tier 2 storage](https://msi.umn.edu/our-resources/knowledge-base/stratus-faqs/what-tier-2-storage)

<!-- For guidance on handling large datasets, please refer to the adapted workflow in the [internal documentation](https://docs.google.com/document/d/1qEC6YwhW-kik2z1EZAlhhUgNSrgH9XlweW-avR00Yls/edit?usp=sharing). -->


