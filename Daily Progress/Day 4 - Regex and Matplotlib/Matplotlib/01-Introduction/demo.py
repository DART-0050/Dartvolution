from matplotlib import pyplot as plt
import snippets
# plt.style.use('fivethirtyeight')
plt.xkcd() #sqiggly lines

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

plt.plot(ages_x, snippets.dev_y,'ok--',label="All Devs")
plt.plot(ages_x, snippets.py_dev_y, marker='o',linestyle='-',color='#8352f6', linewidth=2, label="Python Devs")
plt.plot(ages_x, snippets.js_dev_y,color='#222222', label="JavaScript")

# FORMAT STRINGS
# fmt = '[marker][linestyle][color]'

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plot.png")
plt.show()
