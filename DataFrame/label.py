import pandas as pd 

details = {
    "Name":["Harry","Atom","Kevin"],
    "Cw_marks":[78,89,75]
}

df = pd.DataFrame(details, index = ["S23B13/023", "S23B13/009", "S23B13/007"])

print(df)