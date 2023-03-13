import pandas
import matplotlib.pyplot as plot
import seaborn

# Load the data
red_wine = pandas.read_csv('winequality-red.csv', delimiter=';')
white_wine = pandas.read_csv('winequality-white.csv', delimiter=';')

fig, axes = plot.subplots(ncols=2, figsize=(12,5))
seaborn.histplot(data=red_wine, x='quality', kde=True, ax=axes[0])
seaborn.histplot(data=white_wine, x='quality', kde=True, ax=axes[1])
axes[0].set(title='Red Wine Quality', xlabel='Quality', ylabel='Count')
axes[1].set(title='White Wine Quality', xlabel='Quality', ylabel='Count')
plot.show()
