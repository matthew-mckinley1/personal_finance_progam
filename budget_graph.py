import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def darken_cmap(cmap, factor=0.5):
    """Darken the colormap by a given factor."""
    colors = cmap(np.arange(cmap.N))
    darkened_colors = colors * factor  # Scale RGB values
    return plt.cm.colors.ListedColormap(darkened_colors)

def budget_graph(data):
    df = pd.DataFrame(data)

    # Calculate the difference between Value and Budget
    df['Difference'] = df['Value'] - df['Budget']  # Vectorized calculation

    # Plotting parameters
    categories = df['Category'].unique()
    months = df['Month'].unique()
    num_categories = len(categories)
    bar_width = 0.12
    gap_width = 0.03
    x = np.arange(len(months))

    # Darken the 'gist_rainbow' colormap
    original_cmap = plt.get_cmap('gist_rainbow', num_categories)
    darkened_cmap = darken_cmap(original_cmap, factor=0.85)
    very_darkened_cmap = darken_cmap(original_cmap, factor=0.5)


    fig, ax = plt.subplots(figsize=(12, 6))

    for i, category in enumerate(categories):
        category_data = df[df['Category'] == category]
        offset = bar_width * i - bar_width * (num_categories - 1) / 2 + i * gap_width
        bar_positions = x + offset
        ax.bar(bar_positions, category_data['Value'], bar_width, label=category, color=darkened_cmap(i))

        # Draw budget lines and fill bars
        for j, month_data in category_data.iterrows():
            # Use the 'Difference' column for efficiency
            if month_data['Difference'] < 0:
                ax.bar(bar_positions[category_data.index.get_loc(j)], abs(month_data['Difference']), bar_width, bottom=month_data['Value'], color='#E2E2E2')
            elif month_data['Difference'] > 0:
                ax.bar(bar_positions[category_data.index.get_loc(j)], month_data['Difference'], bar_width, bottom=month_data['Budget'], color=very_darkened_cmap(i))
            if month_data["Budget"] > 0: ax.hlines(month_data['Budget'], xmin=bar_positions[category_data.index.get_loc(j)] - bar_width / 2 - 0.01, xmax=bar_positions[category_data.index.get_loc(j)] + bar_width / 2 + 0.01, color='black', linewidth=3.5)

    ax.set_xticks(x)
    ax.set_xticklabels(months)
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount')
    ax.set_title('Monthly Budget vs. Actual Spending')
    ax.legend()
    plt.tight_layout()
    plt.show()