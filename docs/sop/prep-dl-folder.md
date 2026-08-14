# Prepare DataLad Folder

Here we describe how to prep the project folder you will use to convert to a DataLad repository.

## Create Project Folder

- **Create a project folder on MSI Tier 1 that you will use to convert to your DataLad repository.** 
      - This folder should only include your BIDS data and AWS helper files (see next section) and nothing else!!
      - Name this folder with your `REPO_NAME` defined in the prior step
      - Make sure it is stored in a stable location - this will be the central source of the publicly shared data
- **Store a separate, untouched backup of this folder elsewhere (e.g. in an MSI S3 bucket).** This backup will not be converted to a DataLad repository and is only to be used to recover the data if the DataLad setup becomes corrupted or needs to be rebuilt from scratch.

---

## Add AWS Helper Files

**Add zip archive(s) and an `index.html` to make data easy for users to browse and download.** These additions are optional, but highly recommended because they simplify data access for users and reduce the amount of download documentation you'll need to provide.

- **Create a zip archive**: If the repository is small enough, create a `.zip` of the entire repository for one-click browser downloads (exclude unnecessary files such as `.bidsignore` and `.gitignore`)
- **Add an `index.html`**: Provide a simple interface for browsing folders and downloading files. See the [BOBSRepo `index.html`](https://github.com/DCAN-Labs/bobsrepository/blob/main/index.html) as an example (which renders [here](https://bobsrepository.s3.amazonaws.com/index.html))
- **Update `.bidsignore`**: Add zip archives and index.html files to `.bidsignore` to keep the repository BIDS-valid


