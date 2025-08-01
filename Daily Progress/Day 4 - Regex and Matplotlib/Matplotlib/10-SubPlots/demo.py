
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('C:/Users/Admin/Documents/GitHub/Dartvolution/Daily Progress/Day 4 - Regex and Matplotlib/Matplotlib/10-SubPlots/data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# fig, (ax1, ax2) = plt.subplots(nrows=2,ncols=1)
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_salaries,color='#444444', linestyle='--', label='All Devs')
ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')
ax2.legend()
ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()

fig1.savefig('C:/Users/Admin/Documents/GitHub/Dartvolution/Daily Progress/Day 4 - Regex and Matplotlib/Matplotlib/10-SubPlots/fig1.png')
fig2.savefig('C:/Users/Admin/Documents/GitHub/Dartvolution/Daily Progress/Day 4 - Regex and Matplotlib/Matplotlib/10-SubPlots/fig2.png')