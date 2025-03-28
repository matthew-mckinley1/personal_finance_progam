#Max Holdaway Income / Expenses Entry and Viewing functions
from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator
import pandas

def question(answers,display):
    choice = inquirer.select(
            message=display,
            choices=answers,
            default=None,
            ).execute()
    return choice

def number_input(message):
    input = inquirer.text(
        message=message,
        validate = NumberValidator(message="Please type in a number.")).execute
    return input

def str_input(message):
    input = inquirer.text(
        message=message).execute
    return input


def income_entries(income_entry_list):
    def get_income():
        income_amount = int(number_input('Please type the amount of money you gained:'))
        return income_amount
    def get_income_date():
        income_date = str_input('Please type the date when you got the money:')
        return income_date
    def get_income_source():
        income_source = str_input('Please type where you got the money from:')
        return income_source
    user_income = get_income()
    user_income_date = get_income_date()
    user_income_source = get_income_source()
    income_entry_dict = {'income': user_income, 'income_date': user_income_date, 'income_source': user_income_source}
    income_entry = pandas.DataFrame(income_entry_dict)
    income_entry_list.append(income_entry)
    
def expense_entries(expense_entry_list):
    def get_expense():
        income_amount = int(number_input('Please type the amount of money you spent:'))
        return income_amount
    def get_expense_date():
        income_date = str_input('Please type the date when you spent the money:')
        return income_date
    def get_expense_category():
        income_source = str_input('Please type what you spent the money on:')
        return income_source
    user_expense = get_expense()
    user_expense_date = get_expense_date()
    user_expense_category = get_expense_category()
    expense_entry_dict = {'expense': user_expense, 'expense_date': user_expense_date, 'expense_category': user_expense_category}
    expense_entry = pandas.DataFrame(expense_entry_dict)
    expense_entry_list.append(expense_entry)

def show_income_expense_entry(income_entry_list, expense_entry_list):
    def get_income_entry_date():
        income_entry_date = str_input('Please type the date when you got the money:')
        return income_entry_date
    while True:
        user_input = question(['Income', 'Expense', 'Exit'], 'Choose if you want to see an entry for income or for expense or if you want to exit:')
        if user_input == 'Income':
            user_entry_date = get_income_entry_date()