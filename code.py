import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv('all_data.csv')
data.head(10)

data.info()
data.describe(include = 'all')

print(data.Country.unique())
print(data.Year.unique())
data.Country.replace('United States of America', 'USA', inplace = True)
print(data.Country.unique())

data.rename({'Life expectancy at birth (years)': 'life_expectancy', 'Country': 'country', 'Year': 'year', 'GDP': 'gdp'},
            axis = 'columns', inplace = True)
data.head()

plt.figure(figsize = (5,5))
sns.displot(data.gdp, rug = True)
plt.xlabel('GDP in Trillions of US Dollars')
plt.title('GDP Distribution')
plt.show()
plt.clf()

plt.figure(figsize = (5,5))
sns.displot(data.life_expectancy, rug = True)
plt.xlabel('Life expectancy at birth (years)')
plt.title('Life Expectancy Distribution')
plt.show()
plt.clf()

data_means = data.drop('year', axis = 1).groupby('country').mean().reset_index()
data_means

plt.figure(figsize = (10, 5))
ax1 = plt.subplot(1, 2, 1)
sns.barplot(x = 'country', y = 'gdp', data = data_means)
ax1.set_xticklabels(data_means.country, rotation = 30)
plt.ylabel('GDP in Trillions of US Dollars')
plt.xlabel('Country')
plt.title('Mean GDP for each Country')
ax2 = plt.subplot(1, 2, 2)
sns.barplot(x = 'country', y = 'life_expectancy', data = data_means)
ax2.set_xticklabels(data_means.country, rotation = 30)
plt.xlabel('Country')
plt.ylabel('Life Expectancy at Birth (Years)')
plt.title('Mean Life Expectancy for each Country')
plt.subplots_adjust(wspace = 0.35)
plt.show()
plt.clf()

plt.figure(figsize = (10, 6))
ax1 = plt.subplot(1, 2, 1)
sns.boxplot(x = 'country', y = 'gdp', data = data)
sns.stripplot(x = 'country', y = 'gdp', data = data, size = 5, alpha = 0.5)
ax1.set_xticklabels(data_means.country, rotation = 30)
plt.ylabel('GDP in Trillions of US Dollars')
plt.xlabel('Country')
plt.title('GDP for each Country')
ax2 = plt.subplot(1, 2, 2)
sns.boxplot(x = 'country', y = 'life_expectancy', data = data)
sns.stripplot(x = 'country', y = 'life_expectancy', data = data, size = 5, alpha = 0.5)
ax2.set_xticklabels(data_means.country, rotation = 30)
plt.xlabel('Country')
plt.ylabel('Life Expectancy at Birth (Years)')
plt.title('Life Expectancy for each Country')
plt.subplots_adjust(wspace = 0.25)
plt.show()
plt.clf()


plt.figure(figsize = (8,5))
ax = plt.subplot()
sns.lineplot(x= 'year', y= 'gdp', hue = 'country', data = data)
plt.legend(loc = 'center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.xlabel('Year')
plt.ylabel('GDP in Trillions of US Dollars')
ax.set_xticks(data.year.unique())
ax.set_xticklabels(data.year.unique(), rotation = 30)
plt.show()
plt.clf()


gdp_graph = sns.FacetGrid(data = data, col= 'country', hue = 'country', col_wrap = 3, sharey = False)
gdp_graph = gdp_graph.map(sns.lineplot, 'year', 'gdp').add_legend().set_axis_labels('Year', 'GDP in Trillions of US Dollars')
plt.show()
plt.clf()

plt.figure(figsize= (8, 5))
ax = plt.subplot()
sns.lineplot(x = 'year', y = 'life_expectancy', hue = 'country', data = data)
plt.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), ncol = 1)
plt.xlabel('Year')
plt.ylabel('Life Expectancy at Birth (Years)')
ax.set_xticks(data.year.unique())
ax.set_xticklabels(data.year.unique(), rotation = 30)
plt.show()
plt.clf()


life_expectancy_graph = sns.FacetGrid(data = data, col = 'country', hue = 'country', col_wrap = 3, sharey = False)
life_expectancy_graph = life_expectancy_graph.map(sns.lineplot, 'year', 'life_expectancy').add_legend()\
.set_axis_labels('Year', 'Life Expectancy at Birth (Years)')
plt.show()
plt.clf()

plt.figure(figsize = (10,5))
sns.scatterplot(x = 'life_expectancy', y = 'gdp', hue = 'country', data = data)
plt.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), ncol = 1)
plt.xlabel('Life Expectancy at Birth (Years)')
plt.ylabel('GDP in Trillions of US Dollars')
plt.show()
plt.clf()

gdp_lexpec = sns.FacetGrid(data = data, col = 'country', hue = 'country', col_wrap = 3, sharey = False, sharex = False)
gdp_lexpec = gdp_lexpec.map(sns.scatterplot, 'life_expectancy', 'gdp').add_legend()\
.set_axis_labels( 'Life Expectancy at Birth (Years)', 'GDP in Trillions of US Dollars')
plt.show()
plt.clf()

