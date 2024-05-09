import pandas as pd

a = ["Harry","Atom","Kevin"]

# we can create labels using index function
labels = pd.Series(a, index = ["x","y","z"])

print(labels)

print(labels["x"])