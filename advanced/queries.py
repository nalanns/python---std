import pandas as pd

df = pd.read_csv("people.csv", delimiter=",")
df.set_index("SSN", inplace = True)

# print(df.loc[df["Age"] == 56])
# print(df.loc[df["Age"] < 30])
# print(df.loc[df["Age"] > 30])

print(df.loc[(df["Age"] > 30) & (df["Height"] < 180)]["Name"])


