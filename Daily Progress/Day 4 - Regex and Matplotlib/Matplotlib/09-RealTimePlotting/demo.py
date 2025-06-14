
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count() #counts the number of times the function is called

def animate(i):
    # x_vals.append(next(index))
    # y_vals.append(random.randint(0, 5))  # generates new points

    data = pd.read_csv('C:/Users/Admin/Documents/GitHub/Dartvolution/Daily Progress/Day 4 - Regex and Matplotlib/Matplotlib/09-RealTimePlotting/data.csv', encoding='utf-8')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla() #clears the axis
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
plt.legend(loc='upper left')

ani = FuncAnimation(plt.gcf(), animate, interval=1000) # gcf = Get Current Figure, animate is the function
plt.tight_layout()
plt.show()

