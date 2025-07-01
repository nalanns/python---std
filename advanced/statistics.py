import pandas as pd
import  matplotlib.pyplot as plt
import numpy as np

data = {
    "SSN" : [123, 446, 864, 743],
    "Name" : ["Anna", "Bob", "John", "Mark"],
    "Age"  : [29, 40, 24, 19],
    "Height" : [173, 178, 185, 182],
    "Gender" : ["Female", "Male", "Male", "Male"],
}


df = pd.DataFrame(data)
df.set_index("SSN", inplace=True)

# print(df.count())
# print(df["Age"])
# print(df["Age"].sum())
# print(df.sum()

##########################

# print(df["Height"].mean())
# print(df["Height"].median())
# print(df["Height"].mode())
# print(df["Height"].std())
# print(df["Height"].min())
# print(df["Height"].max())

# print(df["Height"].describe())
print(df.describe())


