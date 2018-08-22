#Copyright @ Somdip Dey, 2018

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

# Style of plot
style_name = 'dark_background'
style.use(style_name)

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
    import sys
    import os.path
    args = False
    try:
        args = sys.argv[1]
    except IndexError:
        args = False
    if(args != False):
        file_name = str(args)
        is_file = os.path.isfile(file_name)
        if is_file == False:
            print('\nError::\n\nWrong file selected! Please, check the path and file name again.\n')
            sys.exit(1)
        main()
    else:
        print('\nError::\n\nNo file selected to read X,Y for plotting!\nPlease, select a file first.\n')
