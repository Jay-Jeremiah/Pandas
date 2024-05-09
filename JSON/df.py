import pandas as pd

data = {
    "Names":{
        "023":"Harry",
        "009":"Atom",
        "007":"Elijah",
        "078":"Perez",
        "075":"Ricky"
    },
    "WebProject":{
        "023":78,
        "009":86,
        "007":79,
        "078":72,
        "075":70
    },
    "LAN":{
        "023":67,
        "009":65,
        "007":70,
        "078":60,
        "075":76
    },
    "DIV":{
        "023":78,
        "009":67,
        "007":86,
        "078":98,
        "075":86
    }
}

df = pd.DataFrame(data)

print(df)