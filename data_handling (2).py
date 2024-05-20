# -*- coding: utf-8 -*-
"""data handling

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ENyMtLHV6iwm0eSd8JTOZY6J0E0VOGG6
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("/content/onlinefoods.csv")

df.info()

df.head()

print(df.describe())

print(df.isnull().sum())

import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

df.hist(bins=30, figsize=(20, 15))
plt.show()
#Histogram

sns.pairplot(df)
plt.show()
#pair

numeric_df = df.select_dtypes(include=['float64', 'int64'])

numeric_df = numeric_df.dropna()

plt.figure(figsize=(12, 8))
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap of Correlation Matrix')
plt.show()
#heat map

plt.figure(figsize=(10, 6))
sns.swarmplot(x='Family size', y='Marital Status', data=df)
plt.title('Swarm Plot of  Family size by Marital Status')


plt.show()
#swarm

plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Feedback', data=df)
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.show()

df.plot(kind='area', alpha=0.4, figsize=(12, 8))
plt.title('Area Plot for All Numeric Features')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='Occupation', y='Age', data=df)
plt.title('Bar Plot of Occupation vs Age')
plt.show()

plt.figure(figsize=(10, 6))
sns.violinplot(x='Occupation', y='Age', data=df)
plt.title('Violin Plot of Occupation vs Age')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Occupation', data=df)
plt.title('Count Plot of Occupation')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Marital Status', y='Age', data=df)
plt.title('Scatter Plot of Marital Status vs Age')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['Feedback'], kde=True)
plt.title('Distribution Plot of Feedback')
plt.show()