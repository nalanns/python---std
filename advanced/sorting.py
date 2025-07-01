import pandas as pd
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

# print(df["Height"].apply(np.sin))
# print(df["Height"].apply(lambda x: x * 100))

# for x in df["Age"]:
#     print(x)

# for key, value in df.items():
#     print("{}: {}".format(key, value))


# for row in df.iterrows():
#     print(row)

###########################

# df.sort_index(inplace=True)
df.sort_values(by=["Name", "Age"], inplace=True)

print(df)
