### NYC Housing Maintenance Code Project

Benny Cohen, Elham Bahrami, Harris Sumra

11/10/2019

In this notebook we will look at the NYC Housing Maintenance Code Project.
The data can be found at https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5


The data describes several housing violations found in NY and provides details including where the incident was,
(broken down by boro, and address), how severe it was (broken down into 3 classes, A,B,C where A is least severe 
and C the most severe)

In this repository we are interested in finding if there are any areas (ie boros) that have a significantly larger number of incidents compared to other boros and/or take a long time to close their incidents . To do this we clean our data, categorize it by answering the 'who, what, and when' about our data and then compare the average time to close incidents. 

We find that although Queens and Brooklyn have a comparatively high number of incidents, they are resolved pretty quickly. We suggest further study about the conditions in the buildings of Queens and Brooklyn to see if the number of incidents is related to how old the buildings are. Right now though no immediate action is needed because incidents are getting resolved. 

This repository contains. 

1. A config folder which lists the columns we are interested in studying. 
(This makes it easy to add and subtract columns without making any code changes.)
2. A data folder which contains our cleaned data
  
  a. filtered.csv - contains all the rows of the columns featured in config/columns.txt
  
  b. clean.csv - contains all rows of incidents which were not postponed

  c. reopened.csv - contains all rows of incidents which were postponed (not actually used in this notebook but kept for future use)

3. A notebook folder which contains our notebooks

   a. HousingCleaning.ipynb shows how we cleaned our data. We removed duplicate rows, changed column types, dealt with nulls, and filtered for the columns we want in this section.

   b. In HousingViolationDataSetEda.ipynb we categorize our data. We show the 'what', namely how most of the incidents in the dataset were closed incidents of medium severity, the 'when', by showing a line plot showing how most incidents occurred toward the end 2014, the ' who and the where' by creating a bar plot of incidents by boro grouping also by the severity of the incident to show how Staten Island did not have so many incidents. We conclude by trying to find a business use case, namely are the number of incidents in a place, related to how long it takes to resolve an incident. We were not able to find any significant difference though. 
 

