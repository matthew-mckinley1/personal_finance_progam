#Darius Vaiaoga, Saving and Loading finances
import csv

# Reads finance file
def read_finances():
    income = []
    expenses = []
    with open('finances.csv', 'r') as finance_file:
        finance_reader = csv.reader(finance_file)

        for row in finance_reader:
            # IF row is not header, add first three value to income list, then add last three to expenses list
            if row != ['income','income_date','income_source',
                       'expense','expense_date','expense_source']:

                income_entry = {'income': row[0], 'income_date': row[1], 'income_source': row[2]}
                # Check if the income_entry is empty, if not, add the income_entry to the income list
                if income_entry != {'income': 0, 'income_date': 0, 'income_source': 0}: 
                    income.append(income_entry)

                expense_entry = {'expense': row[3], 'expense_date': row[4], 'expense_source': row[5]}
                # Check if the expense_entry is empty, if not, add the expense_entry to the expense list
                if expense_entry != {'expense': 0, 'expense_date': 0, 'expense_source': 0}:
                    expenses.append(expense_entry)

    return [income, expenses]

def save_finances(saving_income, data):

    with open('finances.csv', 'a', newline='') as finance_file:
        finance_writer = csv.writer(finance_file)

        if saving_income:
            finance_writer.writerow([data['income'],data['income_date'],data['income_source'],0,0,0])
        else:
            finance_writer.writerow([0,0,0,data['expense'],data['expense_date'],data['expense_source']])
            
    