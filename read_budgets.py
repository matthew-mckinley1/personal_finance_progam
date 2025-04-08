# Reads the budgets, Gabriel Crozier
import csv

def convert_num(num):
    if num:
        num = float(num)
    else:
        num = 0
    return num

def read_budget(location):
    with open(location,'r') as file:
        reader = csv.DictReader(file)
        budgets = {x["category"]:convert_num(x["budget"]) for x in reader}
    return budgets