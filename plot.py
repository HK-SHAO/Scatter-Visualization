import importlib

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def init(data, s, c, t):
    plt.rcParams['figure.figsize'] = (9*1920/1080, 9)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.08)

    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
    ax.invert_yaxis()
    ax.xaxis.set_ticks_position('top')
    ax.yaxis.set_ticks_position('right')
    ax.grid(True, linestyle='-.')

    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)

    i = int(len(c)*s-0.1)
    ax.set_xlabel('{}                       外语分数                {}'.format(c[i], t), fontsize=24)
    ax.set_ylabel('全校排名', fontsize=24)

    xl, yl = [], []
    for d in data:
        x = float(d[1])
        y = float(d[2])
        l = d[0]

        xl.append(x)
        yl.append(y)

        h = str(hash(l))
        color  = [float(h[-13:-9])/1e4, float(h[-9:-5])/1e4, float(h[-5:-1])/1e4]
        plt.scatter(x, y, color = color, s = 90)
        plt.text(x, y, l, fontsize=15, verticalalignment="top", horizontalalignment="right")

    li = np.polyfit(xl, yl, 1)
    x = np.arange(np.min(xl),np.max(xl))
    y = li[0]*x + li[1]
    plt.plot(x, y, linestyle='--', color = 'r')

def re():
    importlib.reload(plt)
