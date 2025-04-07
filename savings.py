# Gabriel Crozier Savings Calcualator
from InquirerPy import inquirer

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

        if action == "create":
            savings_goal = inquirer.number(
                min_allowed=0,
                keybindings=[{"negative_toggle": []}],
                message="Input what you would like to save to"
            )
        elif action == "compare":
            pass
        else:
            break
    
        