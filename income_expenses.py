#Max Holdaway Income / Expenses Entry and Viewing functions
from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator
from dateutil import parser
import save_load

#A function that acts as a template for mulitple user choices as an input
def question(answers,display):
    choice = inquirer.select(
            message=display,
            choices=answers,
            default=None,
            ).execute()
    return choice

#A function that acts as a template for an input checking to make sure the user inputs an integer or float
def number_float_input(message):
    message = message + ' (will get auto rounded to two decimals):'
    while True:
            number = str(inquirer.text(message=message).execute())
            if number.isnumeric():
                number = int(number)
                if number >= 0:
                    return number
                else:
                    print("Number cannot be less than zero.")
            else:
                try:
                    number = float(number)
                    if number >= 0:
                        return round(float(number), 2)
                    else:
                        print("Number cannot be less than zero.")
                except:
                    print("Please type in a number that is not less than zero (you can include decimals).")

#A function that is a simple user input template
def str_input(message):
    input = inquirer.text(
        message=message).execute()
    return input

#The function that gets the income entry from the user
def income_entries():
    #Inner functions for user inputs
    def get_income():
        income_amount = number_float_input('Please type the amount of money you gained')
        return income_amount
    def get_income_date():
        income_date = str_input('Please type the date when you got the money (like MM-DD-YY if any of these are single digits type 0, i.e. 10-04-09:')
        try:
            income_date = parser.parse(income_date)
        except:
            print("Please enter in MM-DD-YY format.")
            income_date = get_income_date()
        return income_date
    def get_income_source():
        income_source = str_input('Please type where you got the money from:')
        return income_source
    user_income = get_income()
    user_income_date = get_income_date()
    user_income_source = get_income_source()
    #The income entry itself
    income_entry_dict = {'income': user_income, 'income_date': user_income_date, 'income_source': user_income_source}
    save_load.save_finances(True, income_entry_dict)
    
#The function that gets the expense entry from the user
def expense_entries():
    #Inner functions for user inputs
    def get_expense():
        income_amount = number_float_input('Please type the amount of money you spent')
        return income_amount
    def get_expense_date():
        income_date = str_input('Please type the date when you got the money (like MM-DD-YY if any of these are single digits type 0, i.e. 10-04-09:')
        try:
            income_date = parser.parse(income_date)
        except:
            print("Please enter in MM-DD-YY format.")
            income_date = get_expense_date()
        return income_date
    def get_expense_category():
        income_source = str_input('Please type what you spent the money on:')
        return income_source
    user_expense = get_expense()
    user_expense_date = get_expense_date()
    user_expense_category = get_expense_category()
    #The expense entry itself
    expense_entry_dict = {'expense': user_expense, 'expense_date': user_expense_date, 'expense_category': user_expense_category}
    
    save_load.save_finances(False, expense_entry_dict)

#A function to find and show a specific entry based on date
def show_income_expense_entry(income_entry_list, expense_entry_list):
    #Inner function for getting the date from the user
    print(income_entry_list)
    print(expense_entry_list)
    def get_entry_date():
        income_entry_date = str_input('Please type the date when you either got the money or spent it (like MM-DD-YY if any of these are single digits type 0(day (less than ten))):')
        try:
            income_entry_date = parser.parse(income_entry_date)
        except:
            print("Please enter in MM-DD-YY format.")
            income_entry_date = get_entry_date()
        return income_entry_date
    while True:
        user_input = question(['Income', 'Expense', 'Exit'], 'Choose if you want to see an entry for income or for expense or if you want to exit:')
        if user_input == 'Income':
            while True:
                user_input = question(['Give a date to use', 'Exit'], 'Choose an option:')
                if user_input == 'Give a date to use':
                    user_entry_date = get_entry_date()
                    #Finding the income entry and if found showing the income entry
                    found = False
                    for income_entry in income_entry_list:
                        if parser.parse(income_entry['income_date']) == user_entry_date:
                            print("The entry has been found showing entry.")
                            print(f'This is the income amount: {income_entry['income']}')
                            print(f'This is the income date: {income_entry['income_date']}')
                            print(f'This is the source of the income: {income_entry['income_source']}')
                            found = True
                    if not found:
                        print("Unable to find any entries with that date please try again.")
                elif user_input == 'Exit':
                    break
        elif user_input == 'Expense':
            while True:
                user_input = question(['Give a date to use', 'Exit'], 'Choose an option:')
                if user_input == 'Give a date to use':
                    user_entry_date = get_entry_date()
                    #Finding the expense entry and if found showing the expense entry
                    found = False
                    for expense_entry in expense_entry_list:
                        if parser.parse(expense_entry['expense_date']) == user_entry_date:
                            print("The entry has been found showing entry.")
                            print(f'This is the expense amount: {expense_entry['expense']}')
                            print(f'This is the expense date: {expense_entry['expense_date']}')
                            print(f'This is the category of the expense: {expense_entry['expense_category']}')
                            found = True
                    if not found:
                        print("Unable to find any entries with that date please try again.")
                elif user_input == 'Exit':
                    break
        elif user_input == 'Exit':
            break
