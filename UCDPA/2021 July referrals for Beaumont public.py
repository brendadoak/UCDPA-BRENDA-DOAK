import pandas as pd
df2021 =pd.read_csv("2021.csv")
df2021=df2021[df2021['Month_Year']=='Jul-21']
df2021=df2021[df2021['Hospital_Name']=='Beaumont Hospital']
print(df2021)