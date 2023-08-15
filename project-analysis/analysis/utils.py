# utils.py

# This file exists to store all necessary functions that will be used across the project.
# Create and test your function in the relevant notebook
# Copy and paste the function here for future use.
# Import utils in any notebook to use these functions

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Data cleaning and preprocessing functions
def remove_duplicates(df):
    """Remove duplicate rows from a DataFrame."""
    return df.drop_duplicates()


def fill_missing_values(df, value):
    """Fill missing values in a DataFrame with a given value."""
    return df.fillna(value)


def convert_to_numeric(df, columns):
    """Convert specified columns in a DataFrame to numeric data type."""
    df[columns] = df[columns].apply(pd.to_numeric, errors="coerce")
    return df


def convert_to_categorical(df, columns):
    """Convert specified columns in a DataFrame to categorical data type."""
    df[columns] = df[columns].astype("category")
    return df


# Data visualization functions
def plot_histogram(data, title, xlabel, ylabel):
    """Plot a histogram for the given data."""
    plt.hist(data, bins=10, alpha=0.7, color="skyblue", edgecolor="black")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def plot_scatter(data, x, y, title, xlabel, ylabel):
    """Plot a scatter plot for the given data."""
    plt.scatter(data[x], data[y], alpha=0.5, color="orange")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def plot_heatmap(data, x_var, y_var, count_var, colour_map):
    """
    Plots a heatmap for two categorical variables, specifically using the count.
    x_var : x-axis variable
    y_var : y-axis variable
    count_var : any other column to perform a count on

    """

    # prepare the data for use
    df = data[[x_var, y_var, count_var]]

    # performing a groupby on the data
    data_count = df.groupby([x_var, y_var]).count()

    # Pivot the data
    data_pivot = data_count.pivot_table(values=count_var, index=y_var, columns=x_var)

    # fill any null value with zero
    data_pivot = data_pivot.fillna(value=0)

    # plot heatmap
    sns.heatmap(data_pivot, cmap=colour_map, annot=True)


# Other utility functions
def save_plot(fig, filename):
    """Save a matplotlib figure to a file."""
    fig.savefig(filename, bbox_inches="tight")


def display_dataframe(df, max_rows=10):
    """Display the first few rows of a DataFrame."""
    display(df.head(max_rows))


def plot_heatmap_new(data, x_var, y_var, target_feature, colour_map = 'RdBu',title = ''):
    '''
    Update to plot_heatmap

    Plots a heatmap for two categorical variables, specifically using the count and mean of a target column. 
    This helps check how to variables relate with respect to a third (numerical variable).

    data: Dataframe containing the data
    x_var : x-axis variable
    y_var : y-axis variable
    target_feature : any other column to perform a count and get the mean.
    
    '''

    #prepare the data for use
    df = data[[x_var, y_var, target_feature]]
    
    # performing a groupby on the data to get the number of occurrences and the average of the target feature by the other features
    data_count = df.groupby([x_var, y_var]).count()
    data_avg = df.groupby([x_var, y_var]).mean()

    #Pivot the count data and fill any null value with zero
    count_pivot = data_count.pivot_table(values = target_feature , index = y_var, columns = x_var)
    count_pivot = count_pivot.fillna(value = 0)

    #Pivot the average data and fill any null value with zero
    avg_pivot = data_avg.pivot_table(values = target_feature , index = y_var, columns = x_var)
    avg_pivot = avg_pivot.fillna(value = 0)

    # Define a custom order for the x and y axes
    x_order = ['Poorly', 'Moderately', 'Very']
    y_order = ['Very', 'Moderately','Poorly' ]

    # Rearrange the pivot tables based on the custom order of columns and index labels
    count_pivot = count_pivot.reindex(columns=x_order, index=y_order)    
    avg_pivot = avg_pivot.reindex(columns=x_order, index=y_order)

     #create axes to plot
    fig, axes = plt.subplots(1, 2, figsize = (15, 5))


    #plot count data and avg data heatmaps
    sns.heatmap(count_pivot,cmap = colour_map, annot = True, ax = axes[0])
    axes[0].set_title('Occurrences')
    sns.heatmap(avg_pivot,cmap = colour_map, annot = True, ax = axes[1])
    axes[1].set_title(f'Average {target_feature}')
    
    #Setting a major title for both plots
    fig.suptitle(f'Overview prep_before vs prep_after {title}', fontsize=16)
    plt.subplots_adjust(wspace=0.8)


def count_and_average(group, avg_col, dataframe):
    '''
    Plots a count and average plot n the same ax
    group: The column to count, group by and get a reference average for.
    avg_col: The column to get the mean for
    ///
    Example: ...
    '''
    
    #getting the average
    avg_course = dataframe.groupby(group).mean().reset_index()

    #Plotting the count and average plots
    plt.figure(figsize = (25, 12))
    ax = sns.countplot(data = dataframe, x=group, label = f'Count of {group} by {group}')
    ax2 = ax.twinx()
    sns.lineplot(x=group, y= avg_col,data = avg_course, ax=ax2, label = f'Average {avg_col} by {group}')
    ax2.set_ylabel(f'average {avg_col}')
    ax2.set_ylim(0, max(avg_course[avg_col]))

    #setting the labels
    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper right')


# Add more functions as needed for your specific project

# Example usage of utility functions
if __name__ == "__main__":
    # Example usage of functions
    data = pd.DataFrame({"A": [1, 2, 3, np.nan, 5], "B": [10, 20, np.nan, 40, 50]})
    print("Original DataFrame:")
    print(data)

    cleaned_data = remove_duplicates(data)
    print("\nDataFrame after removing duplicates:")
    print(cleaned_data)

    filled_data = fill_missing_values(data, value=0)
    print("\nDataFrame after filling missing values:")
    print(filled_data)




