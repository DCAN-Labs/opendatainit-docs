# How To Guide: Open Data Repository Setup
Here we describe the steps required to properly set up an open data repository via the following mechanisms, largely using the [BOBS Repository](https://bobsrepository.readthedocs.io/en/latest/) as an example:

(1) Setting up DataLad repository for versioning and tracking of data provenance        
(2) Making the data repository publicly available via **Amazon AWS** and **OpenNeuro**        

Data can be hosted on AWS via the Amazon Web Services (AWS) Open Data Sponsorship Program, described from their [webpage](https://aws.amazon.com/opendata/open-data-sponsorship-program/) below:

>*The Amazon Web Services (AWS) Open Data Sponsorship Program covers the cost of storage for publicly available high-value cloud-optimized datasets. We work with data providers who seek to:*       

> - *Democratize access to data by making it available for analysis on AWS*
> - *Develop new cloud-native techniques, formats, and tools that lower the cost of working with data*
> - *Encourage the development of communities that benefit from access to shared datasets*

The Amazon Simple Storage Service, or simply [Amazon S3](https://aws.amazon.com/s3/), allows DataLad repository storage for public distribution, management, and tracking. This has several advantages over using private S3 bucket for data repository storage and sharing, including: more robust and better supported utilities supported by Amazon for tracking statistics, scalability, etc. 


## General Requirements

### [De-identification and permission to share publicly](dataprep.md#de-identification-and-permission-to-share-publicly)
### [Format data according to BIDS standards](dataprep.md#bids-standard)
### Amazon AWS: Review Contribution and Community Guidelines
See the [Open Data Registry contribution guidelines](https://github.com/awslabs/open-data-registry/blob/main/CONTRIBUTING.md):
> *The goal of this registry is to expand access to useful data available on AWS. With that in mind, we prefer to list datasets that are clearly documented, are actively supported, can be used for research or educational purposes, and are optimized for analysis using AWS tools. Datasets are included at the discretion of the AWS Open Data team, which may remove datasets from the registry at any time. Data providers are responsible for maintaining and supporting the data that they share.
For more guidance on how to contribute to this registry and what kinds of data are suitable for sharing, please review the [Amazon Open Source Code of Conduct](https://aws.github.io/code-of-conduct) and [AWS Acceptable Use Policy](https://aws.amazon.com/aup/).”