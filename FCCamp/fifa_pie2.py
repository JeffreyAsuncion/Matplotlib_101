import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

fifa = pd.read_csv('fifa_data.csv')


# Pie Chart of Players Weights

fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

# make bins of the different weights
light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa[(fifa['Weight']>=125) & (fifa['Weight']<150)].count()[0]
medium = fifa[(fifa['Weight']>=150) & (fifa['Weight']<175)].count()[0]
medium_heavy = fifa[(fifa['Weight']>=175) & (fifa['Weight']<200)].count()[0]
heavy = fifa[fifa['Weight']>=200].count()[0]

labels = ['under 125', '125-150', '150-175', '175-200', '200 +']
weights = [light,light_medium, medium, medium_heavy, heavy]
explode = [.4, .2, 0, 0, .4]

plt.pie(weights, labels=labels, autopct='%.2f %%', pctdistance=0.75, explode=explode)

plt.title("Weight Distribution of FIFA Players 2018 (lbs)")

plt.show()