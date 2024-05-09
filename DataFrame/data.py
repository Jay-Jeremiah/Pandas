# DataFrame ia table showing organised work

import pandas as pd

data1 = {
    "calories":[420,380,390],
    "duration":[50,40,45]
}

df = pd.DataFrame(data1)

print(df)

# can locate rows using loc atrribute

print(df.loc[0])