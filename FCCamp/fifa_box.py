from matplotlib import colors
import pandas as pd 
import matplotlib.pyplot as plt

fifa = pd.read_csv('fifa_data.csv')

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']

labels = ['FC Barcelona', 'Real Madrid', 'New England Revolution']

boxes = plt.boxplot([barcelona, madrid, revs], labels=labels, patch_artist=True, medianprops={'linewidth':2}) # patch_artist to unlock facecolor

for box in boxes['boxes']:
    # Set edge color
    box.set(color='#4286f4', linewidth=2) 

    # Change Fill Color
    box.set(facecolor='#444441')

plt.title('Profession Soccer Team Comparison')
plt.ylabel('FIFA Overall Rating')


plt.show()