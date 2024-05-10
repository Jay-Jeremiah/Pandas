# inplace will remove all rows containing NULL values 
import pandas as pd

df = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data4.csv')

df.dropna(inplace= True)

print(df.to_string())