# head() reads the top lines of the data set

import pandas as pd 

df = pd.read_csv("C:\\Users\\Jeremiah\\Documents\\CSV_files\\data3.csv")

print(df.head(10))