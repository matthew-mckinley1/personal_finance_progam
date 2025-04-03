# Gabriel Crozier Budget Calculator
from InquirerPy import inquirer


# The selection menu for choosing whether to create / modify a budget
def creation_selection_action(categories):
    print('\033c')
    action_create = inquirer.select(
        message="What would you like to do?",
        choices=[
            "Create New Budget",
            "Modify Old Budget",
            "Exit Creation"
        ],
        filter=lambda result: result.split()[0].lower(),
    ).execute()

    if action_create == "create":
        category = inquirer.text(
            message="What NEW category would you like to add a budget to?",
        ).execute()
    elif action_create == "modify":
        category = inquirer.fuzzy(
            message="Choose a Category to Add a Budget to!",
            # Choices category is first, then it formats it for better reading based on max length, then if there is a current budget print that, else print there isn't
            choices=[f"{x+", ":<{len(max(budgets,key=len))+2}}{f"Currently ${budgets.get(x)}" if x in budgets else "No Current Budget"}" for x in categories],
            filter=lambda result: result.split(",")[0],
            transformer=lambda result: result.split(",")[0],
        ).execute()
    else:
        return None
    return category




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
        category = creation_selection_action(categories)
        print('\033c')
        if category:
            amount = inquirer.number(
                message=f"What would you like to set your budget to?{f" (Currently: ${budgets[category]})" if category in budgets else ""}",
                keybindings={"negative_toggle": []},
                min_allowed=0,
                transformer=lambda result:f"${int(result):,}",
                filter=lambda result: int(result)
            ).execute()

        # Category = "House" or "Rent" for example, amount = 1000, hasn't saved both of those values to savable data or even budget variable yet
        else:
            print("You exited the creation phase")

    elif action == "compare":
        pass
    else:
        return budgets

value1 = {"income":[154,24],"income_dates":[2019,2020],"income_source":["Gas","Food"]}
value2 = {"expense":[14,26],"expence_dates":[2018,2021],"expense_category":["Food","Car"]}

budgets = {"Food":100,"Car":200}

budget(value1,value2,budgets)