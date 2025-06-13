import pandas as pd 
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
#           36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]


data = pd.read_csv('C:/Users/Admin/Documents/GitHub/Dartvolution/Daily Progress/Day 4 - Regex and Matplotlib/Matplotlib/06-Histograms/data.csv', encoding='utf-8')
ages_x = data['Age']
bins = [10,20,30,40,50,60,70,80,90,100]

median_age = 29

plt.axvline(median_age, color="#111111", label="Median Age",linewidth=2) #median age line

plt.legend()
plt.title("Ages of respondants")
plt.xlabel("Ages")
plt.ylabel("Respondants")

plt.hist(ages_x, bins=bins, edgecolor="#000000",log=True)

plt.tight_layout()
plt.show()