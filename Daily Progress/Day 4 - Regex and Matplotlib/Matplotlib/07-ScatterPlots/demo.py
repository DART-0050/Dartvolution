import pandas as pd 
from matplotlib import pyplot as plt

# plt.style.use('fivethirtyeight')

# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
# colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
# sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174, 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

# plt.scatter(x, y, 
#             s=sizes, 
#             alpha=0.5,
#             c=colors, 
#             cmap='Greens', 
#             edgecolor="#000000", 
#             linewidth=1)

data = pd.read_csv('C:/Users/Admin/Documents/GitHub/Dartvolution/Daily Progress/Day 4 - Regex and Matplotlib/Matplotlib/07-ScatterPlots/data.csv', encoding='utf-8')

view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, s=50, c=ratio, cmap='summer', edgecolor="#000000", alpha=0.5)

plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.colorbar(label='Satisfaction') # Display the colours bar

plt.tight_layout()
plt.show()