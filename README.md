### NYC Housing Maintenance Code Project

Benny Cohen, Elham Bahrami, Harrris Sumra

12/1/2019

<em>Summary:</em> In this repository we are interested in finding what areas of NY have the most number of housing violations
and when these incidents occur. We use the <a href="url">NYC Housing Maintenance Code Project dataset</a> with 
the Socrata API. After cleaning the data, making a few visualizations and a statistical test, we conclude 
that although there is no significant difference in where incidents occur, most of them have been raised in the Fall 
in recent years. 

<hr>
<em>Motivation:</em> It is important to keep track of how buildings in New York are being maintained. This means seing
if there are any red flags of areas where an abnormal amount of incidents are occuring.
It also means looking to see if incidents tend to be raised during certain times of year since that can indicate general 
issues in buildings. For example, if many issues are raised during the winter, that may indicate problems with heating.
When incidents occur is also important to keep in mind when the city is figuring out how many people need to be hired
for housing inspections.

<hr>
<em>Methodology:</em>
We do simple data analysis using Python on the <a href="url">NYC Housing Maintenance Code Project dataset</a>

The data describes several housing violations found in NY and provides details including where the incident was,
(broken down by boro, and address), how severe it was (broken down into 3 classes, A,B,C where A is least severe 
and C the most severe)

First we clean our data... Although we don't use all of the columns below in our analysis, we keep them because they can be
used for future study (ie...when the rest of my group decides to get to it.)

We are interested in the following columns...

1. violationid - This uniquely identify incidents. We want to be sure not to duplicate count incidents. 
2. buildingid - This uniquely identifies buildings. This let's us see if some buildings have multiple incidents.
3. boro - Identifies what borough of NY an incident took place in. Important in answering where incidents occur. 
4. zip - the zip code of where an incident took place. Important in answering where incidents occur. 
5. inspectiondate - When an incident was first observed. Important in answering when incidents occur.
6. novdescription - Description of the incident - This can be helpful if we notice an outlier and
need more information about the incident
7. class - The severity of the incident (Values are either A,B or C where A is least severe and C the most severe)
8. currentstatus- The current status of the incident
9. currentstatusdate - The day the incident was updated to its current status. Note that if the current status is closed
we can use this field and the inspection date to see how long it took to close an incident. 

 categorize it by answering the 'who, what, and when' about our data and then compare the average time to close incidents. 

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
 

