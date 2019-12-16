### NYC Housing Maintenance Code Project

Benny Cohen, Elham Bahrami, Haris Sumra

12/1/2019

<strong>Summary:</strong> In this repository we are interested in finding what areas of NY have the most number of housing violations
and when these incidents occur. We use the <a href=https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5>NYC Housing Maintenance Code Project dataset</a> with 
the <a href=https://dev.socrata.com/> Socrata API</a>. After cleaning the data, making a few visualizations and a statistical test, we conclude that most of housing violations have been raised in the Fall 
in recent years. We suspect that it has become part of the city's routine to inspect buildings during the Fall, and advise building owners to
be ready for their inspections before this period. We also note that Queens and Brooklyn have a high number of incidents compared to the other boroughs. This isn't a high priority issue since incidents in these boroughs get resolved in about the same time as other boroughs. We recommend using our data of incidents per year to create a monitor to automatically notify the city if these numbers begin to show anomalies.

<hr>
<strong>Motivation:</strong> It is important to keep track of how buildings in New York are being maintained. This means seing
if there are any red flags of areas where an abnormal amount of incidents are occurring.
It also means looking to see if incidents tend to be raised during certain times of year since that can indicate general 
issues in buildings. For example, if many issues are raised during the winter, that may indicate problems with heating.

<hr>
<strong>Methodology:</strong>
We do simple data analysis using Python on the <a href=https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5>NYC Housing Maintenance Code Project dataset</a>

The data describes several housing violations found in NY and provides details including where the incident was,
(broken down by borough, and address), how severe it was (broken down into 3 classes, A,B,C where A is least severe 
and C the most severe)

First we clean our data... This means choosing which columns we want to study, removing nulls and duplicates, and creating a csv dump of the data that we can use for our analysis. See the <a href = https://github.com/harisx91/NYCHousingMaintenanceCodeProject/blob/master/notebooks/HousingCleaning.ipynb> Housing Cleaning notebook </a> for details.

The meat of our analysis is in the <a href=https://github.com/harisx91/NYCHousingMaintenanceCodeProject/blob/master/notebooks/HousingViolationDataSetEda.ipynb> Housing Violations Eda notebook.</a> We don't have a business question per say when we enter the notebook but are interested in answering the 'who, what, and when' about housing violations to try and find interesting trends or outliers.  
<hr>

This repository contains...

1. A <a href=https://github.com/harisx91/NYCHousingMaintenanceCodeProject/tree/master/notebooks> notebooks folder </a> with the notebooks mentioned above.


2. A <a href=https://github.com/harisx91/NYCHousingMaintenanceCodeProject/tree/master/config> config folder </a> which lists the columns we are interested in studying. 
(This makes it easy to add and subtract columns without making any code changes.)


3. A <a href = https://github.com/harisx91/NYCHousingMaintenanceCodeProject/tree/master/data> data folder </a> which contains our cleaned data
  
  
        a. filtered.csv - contains all the rows of the columns featured in config/columns.txt
  
  
        b. clean.csv - contains all rows of incidents which were not postponed


        c. reopened.csv - contains all rows of incidents which were postponed (not actually used in this notebook but kept for future use)
  
  
        d. dates of opening inspections from 2014-2018


4. The <a href =https://github.com/harisx91/NYCHousingMaintenanceCodeProject/blob/master/HPD_Violation_Open_Data_2017.pdf> description</href> of our data.

<hr>
<strong>Findings and Recomendations:</strong>
The most common incidents have to to with carbon monoxide detectors, painting, and plumbing. Apartment seekers should be on the lookout for these problems when renting apartments. Most incidents have medium severity and are raised in the fall. Also the Bronx has the most number of incidents although most boroughs have around an equal number of incidents. Because there are no outlying areas, no immediate action is needed although we recommend making monitors to automate alerts for if the rate increases above normal levels. We also note some problems with data collection like single buildings having hundreds of incidents and advise the city to improve their data collection process. 
