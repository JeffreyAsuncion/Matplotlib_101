import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

fifa = pd.read_csv('fifa_data.csv')


# Pie Chart of Preferred Foot

left = fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]
right = fifa[fifa['Preferred Foot']=='Right'].count()[0]

labels = ["Left", "Right"]

plt.pie([left, right], labels=labels, autopct='%.2f %%')

plt.title("Foot Preference of FIFA Players 2018")


plt.show()