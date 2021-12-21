import pandas as pd
import numpy as np
df2021=pd.read_csv("UCDPA/2021.csv")
print(df2021)
print(df2021.head)
print(df2021.shape)
missing_values_count= df2021.isnull().sum()
print(missing_values_count[0:100])


