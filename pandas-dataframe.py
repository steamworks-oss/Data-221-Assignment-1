import pandas as pd

# variables
data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}
print(data[0])

# turn dictionary into a dataframe where the keys are now the header of the table and their respective values are the columns
df = pd.DataFrame(data)

# add new column calculated by B^A + C
df["D"] = df["B"] ** df["A"] + df["C"]

# print updated dataframe
print(df)