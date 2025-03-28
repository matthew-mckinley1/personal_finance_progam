#Nicholas Larsen Main Function / User Interface

from InquirerPy import inquirer

def question(answers,display):
    choice = inquirer.select(
            message=display,
            choices=answers,
            default=None,
            ).execute()
    return choice

def main():
    print("Hello! Welcome to your personal finance program!")
    choices = ['1: Track expenses and income.','2: Set budget limits and compare actual spending to limits.','3: Set a savings goal and track progress towards that goal.','4: View data visualizations of income and expenses.','5: Exit']
    choice = question(choices,'This program will help you to:')
    print(choice)
    if choice == choices[0]:
        pass
    elif choice == choices[1]:
        pass
    elif choice == choices[2]:
        pass
    elif choice == choices[3]:
        pass
    else:
        print("Goodbye!")
        exit()