# corr() claculates the relatinship between each column in the data set

import pandas as pd 

fd = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data1.csv')

print(fd.corr())