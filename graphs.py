#Nicholas Larsen graphical displays of income and expenses

import matplotlib.pyplot as mpl
import numpy
import pandas
from InquirerPy import inquirer
def line(type):
    finances = pandas.read_csv('finances.csv')
    finances = finances[finances[f'{type}_date'] != '0']
    finances[f'{type}_date'] = pandas.to_datetime(finances[f'{type}_date'])
    finances.sort_values(by=f'{type}_date',inplace=True)
    finances[f'{type}_date'] = finances[f'{type}_date'].dt.to_period('M')
    grouped = finances.groupby(finances[f'{type}_date'])
    displayed = grouped.sum()
    displayed.plot(y=f'{type}',xlabel='Date')
    mpl.show()

def pie():
    expenses = pandas.read_csv('finances.csv')
    expenses = expenses[expenses['expense_date'] != '0']
    grouped = expenses.groupby(expenses['expense_category'])
    displayed = grouped.sum()
    displayed.plot.pie(y='expense',label='')
    mpl.show()

def graph_ui(income_list, expense_list):
    choice = inquirer.select(
            message='Which would you like to view?',
            choices=['Expense Pie Chart','Income Line graph','Expense Line graph','Exit'],
            default=None,
    ).execute()
    if choice == 'Expense Pie Chart':
        if len(expense_list) == 0:
            print("Please create expense entries first.")
            return
        pie()
    elif choice == 'Income Line graph':
        if len(income_list) == 0:
            print("Please create income entries first.")
            return
        line('income')
    elif choice == 'Expense Line graph':
        if len(expense_list) == 0:
            print("Please create expense entries first.")
            return
        line('expense')
    else:
        return