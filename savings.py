# Gabriel Crozier Savings Calcualator
from InquirerPy import inquirer
from savings_read_write import *

def savings():
    while True:
        action = inquirer.select(
            message="What would you like to do?",
            choices=[
                "Create New Savings Goal",
                "Compare Savings to Goal",
                "Exit Savings",
            ],
            filter=lambda result: result.split()[0].lower()
        ).execute()

        savings_goal = read_savings()
        if action == "create":
            savings_goal = inquirer.number(
                min_allowed=0,
                keybindings=[{"negative_toggle": []}],
                message=f"Input what you would like to save to {f"(Currently: {savings_goal})" if savings_goal else ""}"
            ).execute()
            savings_goal = int(savings_goal)
        elif action == "compare":
            pass
        else:
            write_savings(savings_goal)
            break
    
# Savings is broken, fix at home