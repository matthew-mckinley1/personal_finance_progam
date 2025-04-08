# Gabriel Crozier Budget Calculator
from InquirerPy import inquirer
from budget_graph import budget_graph
from budgets_write import write_budget as wb
from budgets_read import read_budget as rb


months_abr = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")

# This converts the budget data into something usable for my comparer graph (Why was this so awful ):)
def data_converter(expenses_unform, month_year, categories, budgets):
    month, year = month_year.split("-")
    expenses = []

    # Goes through each expense and selects based on the correct month
    for expense in expenses_unform:
        if expense["expense_date"].split(" ")[0].split("-")[0][2:4] == year:
            if expense["expense_date"].split(" ")[0].split("-")[1] == month:
                expenses.append(expense)

    month_label = [months_abr[int(month)]] * len(categories) # Ex: May, May, May, May -- Alows for easy dataframe
    categories = sum([[cat] for cat in categories],[]) # Used to work for multiple months, for now it's just over engineered
    values = [sum([float(ex["expense"]) for ex in expenses if ex["expense_category"] == cat]) for cat in categories] # Goes through each category and adds the sum of all expenses for that category into a list
    budgets_data = sum([[budgets[key]] for key in budgets],[]) # Used to work for multiple months, now it just over engeneered
    
    

    data = {
        'Month': month_label,
        'Category': categories,
        'Value': values,
        'Budget': budgets_data,
    }
    return data



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
def budget(incomes,expenses):
    budgets = rb("budgets.csv") # Gets budgets from budgets.csv

    while True:
        categories = list(dict.fromkeys([x["income_source"] for x in incomes] + [x["expense_category"] for x in expenses] + [key for key in budgets])) # From budgets, incomes, and expenses gets every possible category added
        categories.sort()
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
        
        if action == "create": # Everything to do with messing with budgets
            while True:
                category = creation_selection_action(categories, budgets)
                print('\033c')

                if category:
                    if isinstance(category, list):
                        budgets[category[0]] = None # If budgets is a list than make it a none value
                        continue

                    if not category in categories: categories.append(category)

                    amount = inquirer.number(
                        message=f"What would you like to set your budget to?{f" (Currently: ${budgets[category]})" if category in budgets else ""}",
                        keybindings={"negative_toggle": []},
                        min_allowed=0,
                        transformer=lambda result:f"${int(result):,}",
                        filter=lambda result: float(result)
                    ).execute()

                    # Category = "House" or "Rent" for example, amount = 1000, hasn't saved both of those values to savable data or even budget variable yet
                    budgets[category] = amount # Sets budget to amount, adds budget if needed
                else:
                    break

        elif action == "compare": # Just the graph
            month = inquirer.text(
                message="Choose a month MM-YY",
                validate=lambda result: all([len(result) == 5, result[2] == "-", "".join(result.split("-")).isdigit()]),
                invalid_message="Not Correct Format"
            ).execute()
            data = data_converter(expenses, month, categories, budgets)
            budget_graph(data) # I REALLY WISH I COULD DO MULTIPLE MONTHS BUT THIS WAS ALREADY A NIGHTMARE!!!! # Graphs budgets on month


        else:
            wb("budgets.csv",budgets) # writes to budget after exits returns to main
            return