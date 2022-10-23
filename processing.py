import numpy as np
import matplotlib.pyplot as plt

def preprocess(data, samples):
    sdates, dates = [], []
    samounts, amounts = [], []
    sxcords, xcords = [], []
    sycords, ycords = [], []
    for i in reversed(list(range(len(data)))):
        dates.append(data[i][0])
        amounts.append(data[i][2])
        xcords.append(data[i][1][0])
        ycords.append(data[i][1][1])
    for i in reversed(list(range(len(samples)))):
        sdates.append(samples[i][0])
        samounts.append(samples[i][2])
        sxcords.append(samples[i][1][0])
        sycords.append(samples[i][1][1])
    for i in range(len(dates)):
        dates[i] %= 10080
        if (dates[i] > 7200):
            dates.append(dates[i] - 10080)
            amounts.append(amounts[i])
            xcords.append(xcords[i])
            ycords.append(ycords[i])
        if (dates[i] < 2880):
            dates.append(dates[i] + 10080)
            amounts.append(amounts[i])
            xcords.append(xcords[i])
            ycords.append(ycords[i])
    for i in range(len(samples)):
        sdates[i] %= 10080
    dates = np.array(dates) / 3660
    amounts = np.array(amounts)
    xcords = np.array(xcords)
    ycords = np.array(ycords)

    sdates = np.array(sdates) / 3660
    samounts = np.array(samounts)
    sxcords = np.array(sxcords)
    sycords = np.array(sycords)

    res = [process(dates, amounts, sdates, samounts),
           process(dates, xcords, sdates, sxcords),
           process(dates, ycords, sdates, sycords)]

    return(res)


def process(x, y, x0, y0):
    f = np.polynomial.Polynomial.fit(x, y, 30)
    d = []
    max = 0
    ny = []
    nx = []
    for i in range(len(x)):
        if ( 3 > x[i] > 0):
            d.append(abs(f(x[i]) - y[i]))
            #data = []
            #for j in range(30000):
            #    data.append(f(j/10000))
            #label = list(range(30000))
            #for l in range(len(label)):
            #    label[l] /= 10000
            #plt.plot(label, data)
            ny.append(y[i])
            nx.append(x[i])
    d = np.array(d)
    D = (((d*d).sum() / len(d)) - (d.sum() / len(d))**2)**0.5
    y = np.array(ny)
    x = np.array(nx)
    max=0
    delta = abs(f(x0) - y0)

    return(delta/D, D)