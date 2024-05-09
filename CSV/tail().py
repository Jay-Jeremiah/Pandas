# tail() shows the last lines in the data set
import pandas as pd 

df = pd.read_csv("C:\\Users\\Jeremiah\\Documents\\CSV_files\\data3.csv")

print(df.tail(10))