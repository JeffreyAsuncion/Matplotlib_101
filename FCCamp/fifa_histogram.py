import pandas as pd 
import matplotlib.pyplot as plt

fifa = pd.read_csv('fifa_data.csv')

# print(fifa.head())
# print(fifa.columns)

bins = [40, 50, 60, 70, 80, 90, 100]

plt.hist(fifa.Overall, bins=bins, color='#abcdef')

plt.xticks(bins)

plt.title('Distribution of Player Skills in FIFA 2018')
plt.ylabel('Number of Players')
plt.xlabel('Skill Level')

plt.show()