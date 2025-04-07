# Gabriel Crozier Budget Calculator
from InquirerPy import inquirer
import matplotlib.pyplot as plt

months_abr = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")

# This converts the budget data into something usable for my comparer
def data_converter(expenses, month, categories, budgets):
    # We need months, categories, values, and budgets
    # Each needs to be a list with the same len
    months = [months_abr[(months_abr.index(month) - 2) % 12], months_abr[(months_abr.index(month) - 1) % 12], month] #* 3 # Gets pre month.
    categories = sum([[cat] for cat in categories],[])
    values = [] # need to go through all expenses values and add them up per category per month
    budgets_data = sum([[budgets[key]] for key in budgets],[]) # need to just go through each budget and add it based on categories
    
    print(months)
    print(categories)
    print(values)
    print(budgets_data) # RIGHT NOW ONLY PRINT 6 ITEMS BECAUSE NNEDS TO ADD THE None FEATURE TO BDUDGETS!!
    
    input("gh")
    pass


# The selection menu for choosing whether to create / modify a budget. Makes main budget function less big and confusing
def creation_selection_action(categories, budgets):
    print('\033c')
    action_create = inquirer.select(
        message="What would you like to do?",
        choices=[
            "Create New Budget",
            "Modify Old Budget", # ADD A REMOVE BUDGET OPTION
            "Remove Budget", # IF BUDGETS DOESNT HAVE A VALUE FOR A CATEGORY SET IT TO NONE!!!
            "Exit Creation"
        ],
        filter=lambda result: result.split()[0].lower(),
    ).execute()
    print('\033c')
    
    if action_create == "create":
        category = inquirer.text(
            message="What NEW category would you like to add a budget to?",
        ).execute()

    elif action_create == "modify":
        category = inquirer.fuzzy(
            message="Choose a category to add a budget to!",
            # Choices category is first, then it formats it for better reading based on max length, then if there is a current budget print that, else print there isn't
            choices=[f"{x+", ":<{len(max(budgets,key=len)) + 2}}{f"Currently ${budgets.get(x)}" if budgets.get(x) else "No Current Budget"}" for x in categories],
            filter=lambda result: result.split(",")[0],
            transformer=lambda result: result.split(",")[0],
        ).execute()

    elif action_create == "remove":
        category = inquirer.fuzzy(
            message="Choose a category to remove!",
            # Choices category is first, then it formats it for better reading based on max length, then if there is a current budget print that, else print there isn't
            choices=[x for x in categories],
        ).execute()
        return [category]
    else:
        return None
    return category


# Main budget function. Contains most ui and sets new budgets.
def budget(incomes,expenses,budgets):
    while True:
        categories = list(dict.fromkeys(incomes["income_source"] + expenses["expense_category"] + [key for key in budgets]))
        budgets = {x:budgets.get(x) for x in categories}

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
            while True:
                category = creation_selection_action(categories, budgets)
                print('\033c')

                if category:
                    if isinstance(category, list):
                        budgets[category[0]] = None
                        continue

                    if not category in categories: categories.append(category)

                    amount = inquirer.number(
                        message=f"What would you like to set your budget to?{f" (Currently: ${budgets[category]})" if category in budgets else ""}",
                        keybindings={"negative_toggle": []},
                        min_allowed=0,
                        transformer=lambda result:f"${int(result):,}",
                        filter=lambda result: int(result)
                    ).execute()

                    # Category = "House" or "Rent" for example, amount = 1000, hasn't saved both of those values to savable data or even budget variable yet
                    budgets[category] = amount
                else:
                    break

        elif action == "compare":
            month = inquirer.select(
                message="Month?",
                choices=months_abr
            ).execute()
            data_converter(expenses, month, categories, budgets)
        else:
            print("\033cThank you for using my program!")
            return budgets

value1 = {"income":[154,24],"income_dates":["3/25/25","4/6/25"],"income_source":["Gas","Food"]}
value2 = {"expense":[14,26],"expence_dates":["3/2/28","4/2/25"],"expense_category":["Food","Car"]}

budgets = {"Food":100,"Car":200}

budget(value1,value2,budgets)
print(budgets)