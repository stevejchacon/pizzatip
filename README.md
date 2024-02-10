# Pizza Delivery Driver Tip Analysis

# OUTLINE/DRAFT/NOTES

## Introduction & Project Motivation

The motivation for this project came from the confusions and skepticism for the 
anticipated tip earnings a pizza delivery driver would make during a shift. It
was common and almost guarenteed to hear an inflated estimation of a driver's 
earnings. After some thought, I realized that there was no way of really knowing
unless everything was tracked and due to the fact that this was a source of my 
income, I felt it to be worthwhile for me to do so. I used an app called
HoursTracker where I was able to log when my shift started, when my shift ended,
and the amount of money that I earned in tips during the shift. The most beneficial
feature was the ability to output the file as a .csv in order to be able to run
an analysis when ready. Some of the initial questions and curiosities were things
such as: How much does a driver make per hour? How much does a driver make per
hour on a weekday vs. weekend? Has the increase in menu prices caused an increase
in tips (especially since the customer could tip based on a percentage)? The data
was meticulously tracked from August 3, 2020 - June 24, 2023. The delivery charge
that the customer pay for a delivery was $3 until early July 2021 and raised to $4
thereafter. 

## Methodology & Reasoning
The main goal for this project was not only to run the analysis and the gain the 
proper insights but to also gain as much experience as possible with the various
tools available for data analysis. The hope was to tackle the same analysis in 
multiple ways using matplotlib, seaborn, D3, and Tableau, all of which are very
poplular and powerful within the data analysis space. Not only are these tools and
frameworks used in both academic and professional environments, but they also vary
in their complexity and the challenges that they introduce for a user. They all
have their nuances and are desirabl for different areas of work and research. A
major **disclaimer** is that some of the visualizations created do not actually 
drive a lot of insight. There were moments where a specific visualization would 
not have a lot of impact or provide much meaning but I still found it worthwhile
to create them anyway just for the sole purpose of learning to create different
kinds of visualizations.


## Data

| Column         | Description                                                            | Data Type       |
|----------------|------------------------------------------------------------------------|-----------------|
| Job            | Specifies whether the job was a part of $3/$4 delivery charge time frame | Plain Text      |
| Clocked In     | Time driver punched in for the shift                                   | Time Object     |
| Clocked Out    | Time the driver punched out for a shift                                | Time Object     |
| Duration       | Duration of the shift (in hours)                                       | Float           |
| Earnings       | Amount of money that was earned during a shift                         | Integer         |
| Date           | Date of the shift                                                      | Date Time Object|
| Month          | Numerical month of the shift                                           | Integer         |
| Day            | Numerical day of the shift                                             | Integer         |
| Year           | Numerical year of the shift                                            | Integer         |
| Is Holiday     | True/False of whether the shift was during a holiday                   | Boolean         |
| Holiday Name   | The name of the holiday                                                | Plain Text      |
| Day of Week    | The day of the week for the shift                                      | Plain Text      |
| Hourly Rate    | Calculated hourly rate for the shift                                   | Float           |
| Season         | Season when the shift occurred                                         | Plain Text      |
<br>

## Notebooks & Files
| File                | Description                                         |
|---------------------|-----------------------------------------------------|
| cheatsheet.md       | References to things causing repeated web searching |
| cleanFunc.py        | Functions used during the data cleaning stage       |
| lessons.md          | Lessons learned while doing the project             |
| pizzaCleaning.ipynb | Jupyter Notebook used for cleaning the data         |
| pizzaEDA.ipynb      | EDA using matplotlib #1                             |
| pizzaEDA2.ipynb     | EDA using matplotlib #2                             |
| README.md           | README file for the project                         |
| Reference.ipynb     | References & examples of code found in documentation|
<br>

## Insights

- CHALLENGES -> 




A pizza delivery driver kept track of the tips that they earned during their shifts from August 2020 - December 31, 2022. The "HoursTracker" app was used to clock-in/clock-out for each shift works as well as log the tips earned for the shift. Initial curiosity arose from a discussion amongst the delivery drivers who were speculating how much they actually earned. Like any tip-based job, income fluctuates based on the time of day, the day of the week, and occasion. Occassions can be anything from a holiday to a football game. 


Questions: Are holidays worth working, did the menu price increase & delivery charge increase affect the tips,

explain lack in ability to track when the tips were earned


Approach to the D3 Visualizations:
- While performing this analysis, there was effort made to self study a LinkedIn Learning HTML Essential Training course by Jen Simmons. This beginner course was ideal for trying to learn the foundations of HTML which played a key-role in being able to create the layouts for the D3 visualizations``