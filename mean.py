import pandas as pd  

df = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data6.csv')

x = df["Calories"].mean()

df['Calories'].fillna(x, inplace= True)

print(df.to_string())