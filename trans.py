import csv
import time

import plot

sec = 62
files = ['cz/1.csv', 'cz/2.csv', 'cz/3.csv', 'cz/4.csv']
c = ['高一下期末', '高二上月一', '高二上月二', '高二上期末']
date = ['2018-07-26 06:00:00', '2019-01-26 06:00:00']
p = [3, -2, 0]
n = round((sec*30)/(len(c) - 1))

frames = []
for f in range((len(files)-1)*n):
    frames.append([])

la = []
for l in csv.reader(open(files[-1], encoding='utf-8')):
    la.append(l[p[2]])

for fi in range(len(files) - 1):
    csv1 = csv.reader(open(files[fi], encoding='utf-8'))
    x1, y1, l1 = [], [], []
    for data in csv1:
        x = float(data[p[0]])
        y = float(data[p[1]])
        l = data[p[2]]
        x1.append(x)
        y1.append(y)
        l1.append(l)

    csv2 = csv.reader(open(files[fi + 1], encoding='utf-8'))
    x2, y2, l2 = [], [], []
    for data in csv2:
        x = float(data[p[0]])
        y = float(data[p[1]])
        l = data[p[2]]
        x2.append(x)
        y2.append(y)
        l2.append(l)

    for l in la:
        xi = l1.index(l)
        x0 = x1[xi]
        y0 = y1[xi]

        xi = l2.index(l)
        xe = x2[xi]
        ye = y2[xi]

        for i in range(n):
            s = -2*(i/n)**3+3*(i/n)**2
            xt = x0 + (xe - x0)*s
            yt = y0 + (ye - y0)*s
            frames[n*fi + i].append([l, xt, yt])
            print(n*fi + i, [l, xt, yt])


def trans_time(date, s):
    timeArray = time.strptime(date[0], "%Y-%m-%d %H:%M:%S")
    ts1 = time.mktime(timeArray)

    timeArray = time.strptime(date[1], "%Y-%m-%d %H:%M:%S")
    ts2 = time.mktime(timeArray)

    timeStamp = ts1 + s*(ts2 - ts1)
    timeArray = time.localtime(timeStamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

def save_csv():
    n = 1
    for f in frames:
        csv_write = csv.writer(open('csvs/{}.csv'.format(n), 'w', newline = '', encoding='utf-8'))
        n = n + 1
        for i in f:
            csv_write.writerow(i)

def save_pic():
    n = 0
    for f in frames:
        print('frame:{}'.format(n))

        s = n/len(frames)
        t = trans_time(date, s)
        plot.init(f, s, c, t)
        plot.plt.savefig('pics/{}.png'.format(n), dpi = 120)
        plot.re()
        n = n + 1

    print('frame:{}'.format(n))
    s = n/len(frames)
    t = trans_time(date, s)
    plot.init(frames[-1], s, c, t)
    plot.plt.savefig('pics/{}.png'.format(n), dpi = 120)

save_pic()
