# MIDB Open Data Initiative: Internal SOPs for Setting Up New Repositories

Welcome to the Docs site for setting up a repository via the Masonic Institute for the Developing Brain (MIDB) Open Data Initiative! This initiative links S3 storage, DataLad for version control, and Amazon AWS and OpenNeuro platforms for public access. Data are hosted via the Amazon Web Services (AWS) [Open Data Sponsorship Program](https://aws.amazon.com/opendata/open-data-sponsorship-program/). The Amazon Simple Storage Service, or simply [Amazon S3](https://aws.amazon.com/s3/), allows data storage for public distribution, management, and tracking. 

This documentation is provided to guide MIDB users in setting up an open data repository via MIDB. Using the [BOBS Repository](https://bobsrepository.readthedocs.io) as an example use case, it covers:

(1) Setting up DataLad repository for versioning and tracking of data provenance        
(2) Making the data repository publicly available via **Amazon AWS** and **OpenNeuro**        


**NOTE: Please review the [Open Data Registry contribution & community guidelines](https://github.com/awslabs/open-data-registry/blob/main/CONTRIBUTING.md)**        

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
