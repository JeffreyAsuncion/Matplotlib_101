# Stateful by the state


import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data2.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# Figure is the container holding our plots
# The Axes are the actual plots
fig, ax = plt.subplots()

# now just substitute ax for plt
ax.plot(ages, py_salaries, label='Python')
ax.plot(ages, js_salaries, label='JavaScript')

ax.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Dev')

ax.legend()

# add 'set_'
ax.set_title('Median Salary (USD) by Age')
ax.set_xlabel('Ages')
ax.set_ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()