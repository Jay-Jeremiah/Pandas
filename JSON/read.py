import pandas as pd 

df = pd.read_json("C:\\Users\\Jeremiah\\Documents\\JSON_files\\data.json")

print(df.to_string())