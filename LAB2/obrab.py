import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as mpl
from matplotlib.dates import DateFormatter


nfcom = "nfdump -r nfcapd.202002251200 -o \"fmt:%ts,%sa,%da,%ibyt,%obyt\" | sed \"s/ //g\" | ghead -n -4 > data.csv"
os.system(nfcom)
  
def sum_traf(k, Q):
    return Q * k

def graph(times, values, format=None):
    fig, ax = mpl.subplots(figsize=[15,5])
    ax.plot(times, values)
    DF = DateFormatter(format if format is not None else "%H:%M:%S")
    ax.xaxis.set_major_formatter(DF)
    mpl.title('Зависимость объема трафика от времени')
    mpl.xlabel('Время')
    mpl.ylabel('Всего байт в пакете')
    mpl.gcf().autofmt_xdate()
    mpl.show()

IP_addr = '77.74.181.52'
koef = 1.5

rdcsv = pd.read_csv('data.csv', skiprows=1, header=None)

