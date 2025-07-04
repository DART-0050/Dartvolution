import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('C:/Users/Admin/Documents/GitHub/Dartvolution/Daily Progress/Day 4 - Regex and Matplotlib/Matplotlib/05-FillingAreaLinePlots/data.csv', encoding='utf-8')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries, 
                where=(py_salaries > dev_salaries), #condition
                interpolate=True, #interpolates the line
                alpha=0.25) #transparency

plt.fill_between(ages, py_salaries, dev_salaries, 
                where=(py_salaries < dev_salaries), #condition
                interpolate=True, #interpolates the line
                alpha=0.25) #transparency

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()