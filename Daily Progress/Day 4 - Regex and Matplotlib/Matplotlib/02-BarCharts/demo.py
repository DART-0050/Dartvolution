from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

plt.style.use('fivethirtyeight')

data = pd.read_csv(r'C:\Users\Admin\Documents\GitHub\Dartvolution\Daily Progress\Day 4 - Regex and Matplotlib\Matplotlib\02-BarCharts\data.csv')
ids = data['Responder_id']
languages = data['LanguagesWorkedWith']
language_counter = Counter()

for language in languages:
    language_counter.update(language.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.title("Most Popular Languages")
plt.xlabel("Popularity")

plt.barh(languages, popularity)

plt.tight_layout()
plt.show()



# CODE WITH CSV
# from matplotlib import pyplot as plt
# import numpy as np
# import csv
# from collections import Counter

# plt.style.use('fivethirtyeight')

# with open(r'C:\Users\Admin\Documents\GitHub\Dartvolution\Daily Progress\Day 4 - Regex and Matplotlib\Matplotlib\02-BarCharts\data.csv', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)  #imports the data as dictionary so we can access by keys

#     language_counter = Counter()

#     for row in csv_reader:
#         languages = row['LanguagesWorkedWith'].split(';')
#         language_counter.update(languages)

# # print(language_counter.most_common(15)) #prints the 15 most common languages

# languages = []
# popularity = []

# for item in language_counter.most_common(15):
#     languages.append(item[0])
#     popularity.append(item[1])

# languages.reverse()
# popularity.reverse()

# plt.title("Most Popular Languages")
# plt.xlabel("Popularity")

# plt.barh(languages, popularity)

# plt.tight_layout()
# plt.show()


# CODE WITH X AND Y AXIS
# from matplotlib import pyplot as plt
# import numpy as np
# plt.style.use('fivethirtyeight')

# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# x_indexes = np.arange(len(ages_x)) #numbers the bars from 0 to 10
# width = 0.25

# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]
# plt.bar(x_indexes - width, dev_y, width=width, color="#444444", label="All Devs")

# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]
# plt.bar(x_indexes, py_dev_y, width=width, color="#555555", label="Python")

# js_dev_y = [37810, 43515, 46823, 49293, 53437,
#             56373, 62375, 66674, 68745, 68746, 74583]
# plt.bar(x_indexes + width, js_dev_y, width=width, color="#666666", label="JavaScript")

# plt.xlabel("Ages")
# plt.ylabel("Median Salary (USD)")
# plt.title("Median Salary (USD) by Age")

# plt.legend()
# plt.xticks(ticks=x_indexes, labels=ages_x) #labels the x axis with the ages

# plt.tight_layout()
# plt.show()
