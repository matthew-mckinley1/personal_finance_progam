# Gabriel Crozier Budget Calculator
from InquirerPy import inquirer



def budget(incomes,expenses,budgets):
    categories = list(dict.fromkeys(incomes["income_source"]+expenses["expense_category"]))
    print("\033c")

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

        category = inquirer.fuzzy(
            message="Choose a Category to Add a Budget to!",
            choices=[f"{x+", ":<{len(max(budgets,key=len))+2}}{f"Current Budget: [{budgets.get(x)}]" if x in budgets else "No Current Budget"}" for x in categories],
            filter=lambda result: result.split(",")[0]
        ).execute()

        print(category)
    elif action == "compare":
        pass
    else:
        return budgets

value1 = {"income":[154,24],"income_dates":[2019,2020],"income_source":["Gas","Food"]}
value2 = {"expense":[14,26],"expence_dates":[2018,2021],"expense_category":["Food","Car"]}

budgets = {"Food":100,"Car":200}

budget(value1,value2,{x:budgets[x] for x in budgets})