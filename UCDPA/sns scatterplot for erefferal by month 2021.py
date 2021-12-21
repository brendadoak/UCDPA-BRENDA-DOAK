import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
csv= pd.read_csv('2021.csv')
res=sns.scatterplot(x="Month_Year", y="TotalReferrals", data=csv)
plt.show()