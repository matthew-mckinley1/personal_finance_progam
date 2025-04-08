# Gabriel Crozier, Grpah of savings goal, AI used to help formulate what I needed.

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def data_convertion(incomes,expenses):
    # Convert to DataFrame
    income_df = pd.DataFrame(incomes)
    expense_df = pd.DataFrame(expenses)

    # Convert date strings to datetime objects
    income_df['income_date'] = pd.to_datetime(income_df['income_date'])
    expense_df['expense_date'] = pd.to_datetime(expense_df['expense_date'])

    # Convert income and expense to numeric
    income_df['income'] = pd.to_numeric(income_df['income'])
    expense_df['expense'] = pd.to_numeric(expense_df['expense'])

    # Create a new DataFrame for plotting
    combined_df = pd.DataFrame({
        'date': pd.concat([income_df['income_date'], expense_df['expense_date']]),
        'value': pd.concat([income_df['income'], -expense_df['expense']])  # Expenses as negative values
    })

    # Group by date and sum values
    combined_df = combined_df.groupby('date').sum().reset_index()

    return combined_df


# Graph the sums of all expenses and incomes in one line graph
def graph_savings(incomes,expenses,savings_goal):
    combined_df = data_convertion(incomes,expenses)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the income and expenses
    ax.plot(combined_df['date'], combined_df['value'].cumsum(), marker='o', label='Net Income/Expenses')

    # Add a savings goal line
    if savings_goal:
        savings_goal = float(savings_goal)
        ax.axhline(y=savings_goal, color='#eeaa00', linestyle='--', label='Savings Goal')

    # Formatting the x-axis to show MM-YY
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%m-%y'))
    plt.xticks(rotation=30)

    # Adding titles and labels
    ax.set_title('Income and Expenses Over Time')
    ax.set_xlabel('Date (MM-YY)')
    ax.set_ylabel('Cumulative Amount')
    ax.legend()
    ax.grid()

    # Show the plot
    plt.tight_layout()
    plt.show()