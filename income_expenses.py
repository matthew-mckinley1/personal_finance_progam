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

def number_float_input(message):
    message = message + ' (will get auto rounded to two decimals):'
    while True:
            number = str(inquirer.text(message=message).execute())
            if number.isnumeric():
                return int(number)
            else:
                try:
                    return round(float(number), 2)
                except ValueError:
                    print("Please type in a number (you can include decimals).")

def str_input(message):
    input = inquirer.text(
        message=message).execute
    return input


def income_entries(income_entry_list):
    def get_income():
        income_amount = number_float_input('Please type the amount of money you gained')
        return income_amount
    def get_income_date():
        income_date = str_input('Please type the date when you got the money (like MM/DD/YY if any of these are single digits type 0(day (less than ten))):')
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
        income_amount = number_float_input('Please type the amount of money you spent')
        return income_amount
    def get_expense_date():
        income_date = str_input('Please type the date when you spent the money (like MM/DD/YY if any of these are single digits type 0(day (less than ten))):')
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
    def get_entry_date():
        income_entry_date = str_input('Please type the date when you either got the money or spent it (like MM/DD/YY if any of these are single digits type 0(day (less than ten))):')
        return income_entry_date
    while True:
        user_input = question(['Income', 'Expense', 'Exit'], 'Choose if you want to see an entry for income or for expense or if you want to exit:')
        if user_input == 'Income':
            while True:
                user_input = question[['Give a date to use', 'Exit'], 'Choose an option:']
                if user_input == 'Give a date to use':
                    user_entry_date = get_entry_date()
                    for income_entry in income_entry_list:
                        if income_entry.at('0,', 'income_date') == user_entry_date:
                            print("The entry has been found showing entry.")
                            print(income_entry)
                            break
                    else:
                        print("Unable to find entry please try again")
                        continue
                elif user_input == 'Exit':
                    break
        elif user_input == 'Expense':
            while True:
                user_input = question[['Give a date to use', 'Exit'], 'Choose an option:']
                if user_input == 'Give a date to use':
                    user_entry_date = get_entry_date()
                    for expense_entry in expense_entry_list:
                        if expense_entry.at('0,', 'expense_date') == user_entry_date:
                            print("The entry has been found showing entry.")
                            print(expense_entry)
                            break
                    else:
                        print("Unable to find entry please try again")
                        continue
                elif user_input == 'Exit':
                    break
        elif user_input == 'Exit':
            break
