import pandas as pd
df2021= pd.read_csv("2021.csv")
print(df2021)
print(df2021.head)
print(df2021.shape)
drop_duplicates= df2021.drop_duplicates()
print(df2021.shape,drop_duplicates.shape)