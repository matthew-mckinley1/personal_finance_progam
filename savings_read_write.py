# Reads and writes to savings files

def read_savings():
    with open("savings.txt","r") as file:
        savings_goal = file.read()
        try: savings_goal = int(savings_goal)
        except: print("Error in Savings")
    return savings_goal

def write_savings(savings_goal):
    with open("savings.txt","w") as file:
        file.write(savings_goal)