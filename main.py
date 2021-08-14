import numpy as np
import pandas as pd
import matplotlib as mb

df = pd.read_csv('SeattleListings.csv')
print(df.head())


rows = df.shape[0]
columns = df.shape[1]
nullColumns=df.columns[df.isna().any()==True]
allColumns = df.columns

#What's the shape of the data
print("rows: " + str(rows)) #How many rows
print("columns: " + str(columns)) #How many columns


#How many columns have missing values
no_nulls = df.isna().any().sum() #How many columns with missing values?
perc_col_nulls = df.isna().any().sum()/df.shape[1] #What % of the columns have missing data?
print ("Columns with missing data:" + str(no_nulls))
print ("Percentage of columns with null values: " + str(perc_col_nulls*100))
print("List of all columns in dataset: " + str(allColumns))
print ("List of all columns with nulls: " + str(nullColumns))

''' Questions:

What's the average price for AirBnB in Seattle?

Which locations have the least number of stays and how does this relate to the host response rate?

How does the review score correlate with the price?

'''


