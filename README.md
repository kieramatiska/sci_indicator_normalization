# sci_indicator_normalization

This is a github repository (repo) normalizing indicator values for a Surf Conservation Index (SCI) in the country of Brazil. Two SCIs were created, one including an ecosystem services assessment, called the climate index, and one without. The files contain a sensitivity analysis (10km, 5km, and 1km) and an analysis for different regions (all of Brazil, North-Northeast (nne), Southeast (se), and South (s)). The structure of this repo is below.

## File System Setup

Below are the files in the repo and what each one contains.

### Data Folder (data)

This folder is split into 8 different subfolders, listed below, and contains 1 .csv file not located in a folder, "sci_difference.csv". All data in the subfolders were imported into R from ArcGIS Pro. Each .csv file contains numbers indicating the amount of each locator found within a surf break buffer.

- pressure folder: Contains indicators for built area, human modification, population change, roads, and ports
- biodiversity folder: Contains indicators for coral reefs, mangroves, seagrass, marine and terrestrial species richness, oceanic priority areas, terrestrial priority areas ranked high, very high, and extremely high, and tree cover
- surf folder: Contains one .csv with all surf indicator values
- social folder: Contains indicators for airports, employment in the leisure and tourism industry, and hotels
- climate folder: Contains one .csv with all climate indicator values
- response folder: Contains indicators for UNESCO biosphere reserves (atl_forest_pa.csv), bandeira azul beaches, protected areas, RAMSAR (internationally important wetland) sites, UNESCO world heritage sites, and world surfing reserves
- surf_spot_states folder: Contains one .csv that assigns each surf break with a state
- sensitivity_analysis folder: split into 2 folders (1km and 5km) with each folder split into 5 folders (pressure, biodiversity, surf, social, and response) that contain the indicators listed above

### Output Normalized Tables Folder (normalized_csvs)

This folder is split into 8 different subfolders, listed below.

- pressure folder: contains the normalized pressure index values for all of Brazil and each subregion, and is split into two additional subfolders to separate the 1km and 5km normalized files.
- biodiversity folder: contains the normalized biodiversity index values for all of Brazil and each subregion, and is split into two additional subfolders to separate the 1km and 5km normalized files.
- surf folder: contains the normalized surf index values for all of Brazil and each subregion, and is split into two additional subfolders to separate the 1km and 5km normalized files.
- climate folder: contains the normalized climate index values for all of Brazil and each subregion, and is split into two additional subfolders to separate the 1km and 5km normalized files.
- response folder: contains the normalized response index values for all of Brazil and each subregion, and is split into two additional subfolders to separate the 1km and 5km normalized files.
-sci folder: split into two subfolders ("sci_w_climate"" and "sci_wo_climate") that contains the normalized values for the specific sci the folder refers to for all of Brazil and each subregion, and is split into two additional subfolders to separate the 1km and 5km normalized files
- all data folder: contains two files, one with all normalized data without the sensitivity analysis ("all_data.csv") and one with all normalized data with the sensitivity analysis ("all_data_sa.csv")

### RMarkdown folder (Rmds)

This folder contains four .Rmds, listed below.

- "indicator_normalization.Rmd": this file takes all the data in the each of the index folders and normalizes them to get normalized index values and SCI values with and without the Climate Index for all of Brazil and each subregion
- "results.visualization.Rmd": this file visualizes the index values for each surf break with the sensitivity analysis through histograms, other graphs, and tables.
- "sensitivity_analysis_1km.Rmd": this file does the same thing as the "indicator_normalization.Rmd", but only at a 1km scale
- "sensitivity_analysis_5km.Rmd": this file does the same thing as the "indicator_normalization.Rmd", but only at a 5km scale

Each .Rmd file has comments regarding what the code is doing and what should occur depending on the analysis. For example, if finding a normalized biodiversity index score for the sourthern region, you would want to uncomment the code for the coral reef indicator as there are not coral reefs on the Southern coast of Brazil.

## Contributors

Kiera Matiska: Bren School of Environmental Science & Management
Kort Alexander: Bren School of Environmental Science & Management

## Use

Anyone is able to fork/clone this repo for their own work. 

Note: The SCI is a novel instrument constructed by Save the Waves Coalition for surf conservation and is now used by the Surf Conservation Partnership (a partnership between the coalition and Conservation International). This code should only be used for future SCI work.
