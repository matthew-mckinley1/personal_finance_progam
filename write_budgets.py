# File to write the budgets to a csv
import csv

def write_budget(location,budgets):
    budgets = [{"category":x,"budget":budgets[x]} for x in budgets]
    with open(location,'w',newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["category","budget"])
        writer.writeheader()
        writer.writerows(budgets)