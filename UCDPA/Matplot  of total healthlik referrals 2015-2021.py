from typing import List
import matplotlib.pyplot as plt
year = ['2015','2016','2017','2018','2019','2020','2021']
referrals = [16969,115495,53063,354819,540328,2163223,2847339]
plt.xlabel('year')
plt.ylabel(' total erefferals')
plt.plot(year,referrals)
plt.show()
