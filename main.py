import numpy as np
import pandas as pd
import matplotlib as mb

#Import Seattle AirBnB Data
survey = pd.read_csv('SeattleListings.csv')
price = pd.read_csv('SeattleCalendar.csv')
review = pd.read_csv('SeattleReviews.csv')

print (survey.head())
print (price.head())
print (review.head())

#Survey Data Checks - how much data is available and what's missing
surveyRows = survey.shape[0]
surveyColumns = survey.shape[1]
nullSurveyColumns=survey.columns[survey.isna().any()==True]
allSurveyColumns = survey.columns


#Rows and Columns
print("survey_rows: " + str(surveyRows)) #How many survey_rows
print("survey_columns: " + str(surveyColumns)) #How many survey_columns

#How many survey_columns have missing values
no_nulls = survey.isna().any().sum() #How many survey_columns with missing values?
perc_col_nulls = survey.isna().any().sum()/survey.shape[1] #What % of the survey_columns have missing data?
print ("survey_columns with missing data:" + str(no_nulls))
print ("Percentage of survey_columns with null values: " + str(perc_col_nulls*100))
print("List of all survey_columns in dataset: " + str(allSurveyColumns))
print ("List of all survey_columns with nulls: " + str(nullSurveyColumns))


#price Data Checks - how much data is available and what's missing
priceRows = price.shape[0]
priceColumns = price.shape[1]
nullpriceColumns=price.columns[price.isna().any()==True]
allpriceColumns = price.columns


#Rows and Columns
print("price_rows: " + str(priceRows)) #How many price_rows
print("price_columns: " + str(priceColumns)) #How many price_columns

#How many price_columns have missing values
no_nulls = price.isna().any().sum() #How many price_columns with missing values?
perc_col_nulls = price.isna().any().sum()/price.shape[1] #What % of the price_columns have missing data?
print ("price_columns with missing data:" + str(no_nulls))
print ("Percentage of price_columns with null values: " + str(perc_col_nulls*100))
print("List of all price_columns in dataset: " + str(allpriceColumns))
print ("List of all price_columns with nulls: " + str(nullpriceColumns))



''' Questions:

What's the average price for AirBnB in Seattle?

Which locations have the least number of stays and how does this relate to the host response rate?

How does the review score correlate with the price?

'''


