# Reads and writes to savings files

def read_savings():
    with open("savings.txt","r") as file:
        savings_goal = file.read()
        try: savings_goal = float(savings_goal)
        except: pass
    return savings_goal # Reads savings and returns as a float if possible

def write_savings(savings_goal):
    with open("savings.txt","w") as file:
        file.write(savings_goal) # Overrides whole file with new savings goal