# replacing values in a wrong format using loc[]

import pandas as pd

de = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data8.csv')

de.loc[7, 'Duration'] = 45

de.loc[14, 'Calories'] = 345.1

de.loc[8, 'Date'] = '2024/12/21'


print(de.to_string())