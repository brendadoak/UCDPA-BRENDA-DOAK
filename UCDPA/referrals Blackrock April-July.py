
from typing import List
import matplotlib.pyplot as plt
Month = ["April","May","June","July"]
Referrals = [1732,753,890,1644]
plt.xlabel('Month')
plt.ylabel('Referrals to Blackrock')
plt.plot(Month, Referrals)
plt.show()



