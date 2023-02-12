# ASUU Strike Impact Mock Analysis

This project aims to analyze the impact of the ASUU strike on students at the University of Lagos (UNILAG). The goal is to gain insights into how the strike affected the students, their academic performance, and overall wellbeing. This is a mock analysis of the project before data is collected from the public.

## Contents

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Model Building
- Evaluation
- Communication

## Data Preprocessing

The first step in this project is to clean the data and prepare it for analysis. This includes removing all non-UNILAG students, dropping unrequired columns, and renaming the columns to make them more descriptive. Outliers such as 100 level students and CGPA values of 0 are also removed. A target variable (cgpa_change) is calculated as the difference between the CGPA before and after the strike.

### Observations

1. Survey should be checked for inconsistencies before publishing. Especially the "Level" question.

## Exploratory Data Analysis (EDA)

The EDA stage involves analyzing the data visually to gain insights into the relationships between variables and to identify patterns and trends. Various plots such as histograms, bar plots, and scatter plots can be used to explore the data.

## Model Building

The next step is to build a predictive model to determine the factors that influence a student's CGPA after the strike. This includes selecting appropriate features, splitting the data into training and testing sets, and selecting an appropriate algorithm. The goal is to determine the factors that are most predictive of a student's CGPA after the strike.

## Evaluation

The model is evaluated using appropriate metrics such as accuracy, precision, recall, and F1 score. The model's performance is compared to a baseline to determine if it is an improvement over a simple model.

## Communication

The final step is to communicate the findings of the analysis. This includes creating visualizations, writing a report, and presenting the results in a clear and concise manner. The goal is to make the findings accessible to a wider audience and to provide actionable insights to stakeholders.
