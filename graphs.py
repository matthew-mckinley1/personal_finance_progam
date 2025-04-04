#Nicholas Larsen graphical displays of income and expenses

import matplotlib.pyplot as mpl
import numpy
import pandas

finances = pandas.read_csv('finances.csv')
finances = finances[finances['income_date'] != '0']
finances['income_date'] = pandas.to_datetime(finances['income_date'])
finances.sort_values(by='income_date',inplace=True)
finances['income_date'] = finances['income_date'].dt.to_period('M')
grouped = finances.groupby(finances['income_date'])
displayed = grouped.sum()
print(displayed)
displayed.plot(y='income',xlabel='Date')
mpl.show()
