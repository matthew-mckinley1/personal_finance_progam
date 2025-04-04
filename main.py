#Nicholas Larsen Main Function / User Interface

from InquirerPy import inquirer
from login import *
from income_expenses import *
from graphs import *
from currencies import *
from save_load import read_finances
def question(answers,display):
    choice = inquirer.select(
            message=display,
            choices=answers,
            default=None,
            ).execute()
    return choice

def main():
    print("Hello! Welcome to your personal finance program!")
    login()
    choices = ['1: Track expenses and income.','2: Set budget limits and compare actual spending to limits.','3: Set a savings goal and track progress towards that goal.','4: View data visualizations of income and expenses.','5: Exit']
    choice = question(choices,'This program will help you to:')
    print(choice)
    if choice == choices[0]:
        which = question(['Expenses','Income','View'],'Would you like to input income or expenses, or view previous entries?')
        if which == 'Expenses':
            expense_entries(read_finances()[1])
        else:
            income_entries(read_finances()[0])
    elif choice == choices[1]:
        pass
    elif choice == choices[2]:
        pass
    elif choice == choices[3]:
        pass
    else:
        print("Goodbye!")
        exit()

