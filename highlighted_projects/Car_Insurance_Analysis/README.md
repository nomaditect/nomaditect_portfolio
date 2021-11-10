# Car_Insurance_Prediction

by [Simon Stewart](https://github.com/nomaditect), October 2021


## Predicting car insurance claim amounts - a linear regression Case Study

## Table of content
- [Project Brief](https://github.com/lillaszulyovszky/ironhack-case-study-classification/blob/main/README.md#project-brief)
- [Data](https://github.com/lillaszulyovszky/ironhack-case-study-classification/blob/main/README.md#data)
- [Process & Tools](https://github.com/lillaszulyovszky/ironhack-case-study-classification#process--tools)
- [Visualization](https://github.com/lillaszulyovszky/ironhack-case-study-classification#visualizations)
- [Key Take Aways](https://github.com/lillaszulyovszky/ironhack-case-study-classification#key-take-aways)

## Scenario: 

We are risk analysts employed at a bank. Our team is focusing on credit card services. We are given data from 18.000 of our customers and our boss wants us to work out how we can improve our credit card marketing campaign.

## Challenge: 
Use the given data set to find out what characteristics impact the customers decision on accepting or declining our credit card offer.

## Problem: 
Can we build a machine learning model that predicts if our customer accepts or declines the credit card offer?


Further project details such as deliverables can be found here

# Data
Leveraging on the data we were provided with, we used Tableau's and Python's data visualisation tools to explore the relationships between features.

To find out more about the distribution of the important features we highlighted, you can have a look on our Tableau dashboard below:
Tableau Dashboard

For further details on all features, please refer to the notebook.

# Process & Tools

## Process

Our ways of working included an iterative/agile approach circling through the following steps:

## workflow

Github: set up our Github repo to collaborate on. We did 104 commits in 4 days.
Trello: set up our Trello board to help us keep sane and reprioritise daily.
SQL: started with the independent task of completing the SQL queries
EDA: assessment of dataframe to prepare for cleaning
Data cleaning & wrangling in Python: drop 'customer_number' column, drop null values, convert float columns to int
Prepocessing: 3 methods - Normalizer, Dummies and SMOTE
Machine Learning Model: using scikit learn
- iteration 1 (X): In our first iteration we only used preprocessing and encoding and used this as a benchmark for the following iterations as comparison
- iteration 2 (X_i2): SMOTE sampling to improve the imbalance of the target
- iteration 3 (X_i3): dropping quarterly balance columns to reduce noise
- iteration 4 (X_i4): encoding numerical features to categorical ones
- iteration 5 (X_i5): using KNN on the i3

## Tools + Libraries

* Database: [car_insurance_cleaned_dataset](https://github.com/nomaditect/nomaditect_portfolio/tree/main/highlighted_projects/Car_Insurance_Analysis/Datasets)
* Vizualizations: seaborn / matplotlib
* Code: Jupyter Notebook - Link to code folder
* Visualizations: Python

## Key Take Aways

* The model was able to predict a claim amount of +/- 9,314.34 USD @ 77.7% prediction rate
* Upgrade: replace 0 income with a mean variable? # run a forloop replacing 0 with mean.
* Personally i have little to no faith in this model, but hey it was fun!


Thank you for reading!
If you have any questions, please reach out to us.
