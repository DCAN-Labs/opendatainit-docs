# Internal SOP: MIDB Open Data Repository Setup

Welcome to the Docs site for setting up a repository via the Masonic Institute for the Developing Brain (MIDB) Open Data Initiative! This initiative links S3 storage, DataLad for version control, and Amazon AWS and OpenNeuro platforms for public access. This documentation is provided to guide internal MIDB users in setting up an open data repository via MIDB. Using the [BOBS Repository](https://bobsrepository.readthedocs.io) as an example use case, it covers:

(1) Setting up DataLad repository for versioning and tracking of data provenance        
(2) Making the data repository publicly available via **Amazon AWS** and **OpenNeuro**        

## General Requirements
- **Make sure that the data folder is located on MSI tier1 storage**: see [NOTE: For Small Data Repositories Only](datalad-init.md#note-for-small-data-repositories-only) for details
- **[De-identification and permission to share publicly](dataprep.md#de-identification-and-permission-to-share-publicly)**        
- **[Format data according to BIDS standards](dataprep.md#bids-standard)**        
- **Amazon AWS: Review [Open Data Registry contribution & community guidelines](https://github.com/awslabs/open-data-registry/blob/main/CONTRIBUTING.md):**        
> *The goal of this registry is to expand access to useful data available on AWS. With that in mind, we prefer to list datasets that are clearly documented, are actively supported, can be used for research or educational purposes, and are optimized for analysis using AWS tools. Datasets are included at the discretion of the AWS Open Data team, which may remove datasets from the registry at any time. Data providers are responsible for maintaining and supporting the data that they share.*     
> *For more guidance on how to contribute to this registry and what kinds of data are suitable for sharing, please review the [Amazon Open Source Code of Conduct](https://aws.github.io/code-of-conduct) and [AWS Acceptable Use Policy](https://aws.amazon.com/aup/).*

## Checklist

Below is a checklist of the essential tasks outlined in this Docs website. Feel free to make a copy for yourself for tracking purposes!

**General requirements:**       
<input type="checkbox"> Read through contents of this Docs website      
<input type="checkbox"> Ensure that permissions to share publicly are in place (e.g. completing a data use agreement)       
<input type="checkbox"> Complete any de-identification necessary for your specific data     
<input type="checkbox"> Ensure that data is in BIDs format  

**Initialize AWS Bucket:**      
<input type="checkbox"> Link to MIDB Account                    
<input type="checkbox"> Create YAML File        
<input type="checkbox"> Create Tutorial     
<input type="checkbox"> Submit Pull Request     
<input type="checkbox"> AWS Bucket Configuration

**Set up DataLad using Amazon S3 as special remote:**  
<input type="checkbox"> Complete initial setup and requirements steps  
<input type="checkbox"> Complete steps to initialize DataLad repository  
<input type="checkbox"> Add Amazon S3 as special remote         
<input type="checkbox"> Create GitHub Sibling and Publish       
<input type="checkbox"> Add OpenNeuro as a GitHub sibling   
