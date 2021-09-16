# This program was written pn python 3.9.7
# Install pandas: py -m pip install pandas

import pandas as pd
import os

#Part 1

#Downloads the csv data file at https://gist.github.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2 as "raw" and reads the file into a program memory.
url = 'https://gist.githubusercontent.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2/raw/279b794a834a62dc108fc843a72c94c49361b501/data.csv'

#Once the data is read into memory it prints out how many rows of the data is in the CSV data.
df = pd.read_csv(url)

print('\nThis is how many rows of the data that are in the CSV file: ' + str(f"{len(df),}") + ' Rows.')


#Then it removes all the rows with 'profit' that are not a numerical value.
df['Profit (in millions)'] = pd.to_numeric(df['Profit (in millions)'], errors='coerce')

#Then it prints out how many rows of data are left, after removing all the rows with invalid non-numeric profit column data. 
df = df.dropna(subset=['Profit (in millions)'])

print('\nThis is how many rows of the data that are in the CSV data after removing all rows with profit that is not numerical value: ' + str(f"{len(df):,}") + ' Rows.')


#Part 2

#Converts the contents read into memory into JSON format and writes it out to a file called data2.json which only contains rows of data that have the valid numeric profit values. Each row in the Array contains data columns like year, rank, company, revenue, and profit.
with open('data2.json', 'w') as f:
    f.write(df.to_json(orient='records', lines=True))

#Orders the data based on the profit value.

df = df.sort_values(["Profit (in millions)"], ascending=False)


#Prints the top 20 rows with the highest profit values 


df = df.nlargest(20,'Profit (in millions)',keep='all')

print("\nThe top 20 rows with the highest profit values:\n")

print(df)
