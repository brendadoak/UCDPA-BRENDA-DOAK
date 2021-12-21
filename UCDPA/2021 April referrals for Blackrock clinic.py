import pandas as pd
df2021 =pd.read_csv("2021.csv")
df2021=df2021[df2021['Month_Year']=='Apr-21']
df2021=df2021[df2021['Hospital_Name']=='Blackrock Clinic']
print(df2021)

