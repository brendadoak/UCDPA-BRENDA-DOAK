from typing import List
import matplotlib.pyplot as plt
Month = ["April","May","June","July"]
Referrals= [5635,2402,3621,5562]
plt.xlabel('Month')
plt.ylabel('Referrals to Beaumont')
plt.plot(Month, Referrals)
plt.show()