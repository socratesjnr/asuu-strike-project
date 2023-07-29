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
