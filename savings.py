# Gabriel Crozier Savings Calcualator
from InquirerPy import inquirer
from savings_read_write import *
from savings_graph import graph_savings


# Savings UI
def savings(incomes,expenses):
    while True:
        print('\033c')
        action = inquirer.select(
            message="What would you like to do?",
            choices=[
                "Create New Savings Goal",
                "Compare Savings to Goal",
                "Exit Savings",
            ],
            filter=lambda result: result.split()[0].lower()
        ).execute()

        read_savings_goal = read_savings()
        print("\033c")

        # Create function just makes savings goal a specific value
        if action == "create":
            savings_goal = inquirer.number(
                min_allowed=0,
                keybindings={"negative_toggle": []},
                message=f"Input what you would like to save to {f'(Currently: ${read_savings_goal})' if read_savings_goal else ''}" # Message adds a currently if there is a current savings goal
            ).execute()

            write_savings(savings_goal) # Writes at the end
        elif action == "compare":
            graph_savings(incomes,expenses,read_savings_goal)
        else:
            break