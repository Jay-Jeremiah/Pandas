# we use median() attribute to calculate the median

import pandas as pd 

trial = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data6.csv')


y = trial.median()

print(y)