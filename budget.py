# Gabriel Crozier Budget Calculator
from InquirerPy import inquirer


def budget(incomes,expenses,budgets):
    print(budgets)
    action = inquirer.select(
        message="What would you like to do?",
        choices=[
            "Create Budget",
            "Compare Budgets",
            "Exit Program"
        ],
        filter=lambda result: result.split()[0].lower(),
    ).execute()

    if action == "create":
        pass
    elif action == "compare":
        pass
    else:
        return budgets

value1 = {"income":[154,24],"income_dates":[2019,2020],"income_source":["Gas","Food"]}
value2 = {"expense":[14,26],"expence_dates":[2018,2021],"expense_category":["Food","Car"]}

budgets = [1,2,3]
budgets_good = value1["income_source"]+value2["expense_category"]

budget(value1,value2,{x:"Hi" for x in budgets_good})