#live_plot
#Copyright @ Somdip Dey, 2018

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def main():
    plt.rcParams['agg.path.chunksize'] = 10000
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

def animate(i):
    graph_data = open(file_name,'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)

if __name__ == '__main__':
    file_name = 'ex1.txt'
    main()
