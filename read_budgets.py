# Reads the budgets, Gabriel Crozier
import csv

def read_budget(location):
    with open(location,'r') as file:
        reader = csv.DictReader(file)
        budgets = {x["category"]:x["budget"] for x in reader}
    return budgets