import pandas as pd
import numpy as np
from datetime import datetime

data = pd.read_csv("dsc_fc_summed_spectra_2023_v01.csv")

data['vector1'] = pd.to_numeric(data['vector1'])
data['vector2'] = pd.to_numeric(data['vector2'])
data['vector3'] = pd.to_numeric(data['vector3'])

data['date'] = pd.to_datetime(data['date'])

data['time'] = data['date'].dt.strftime("%H")
data['date'] = data['date'].dt.strftime("%d/%m/%Y")

data2 = data.groupby(['date','time']).sum()

data3 = pd.read_csv('kindex.txt', header=None, delimiter=r'\s+', names='year month date hour value1 value2 value3 Kp value4 value5'.split(' '))