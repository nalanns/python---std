import pandas as pd
import  matplotlib.pyplot as plt
from numpy import dtype

data = {
    "SSN" : [123, 446, 864, 743],
    "Name" : ["Anna", "Bob", "John", "Mark"],
    "Age"  : [29, 40, 24, 19],
    "Height" : [173, 178, 185, 182],
    "Gender" : ["Female", "Male", "Male", "Male"],
}

df = pd.DataFrame(data)
df.set_index("SSN", inplace=True)
# print(df)

# print(df.head(2))
# print(df.tail(2))
# print(df.ndim)
# print(df.shape)
# print(df.size)
# print(df.index)
# print(df.dtypes)
# print(df.T)

##########################
# print(df["Name"].iloc[1])
# print(df.iloc[0:2])

# df.plot.bar()
df.Age.hist()
plt.show()
