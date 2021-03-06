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
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()


ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Dev')


# now just substitute ax for plt
ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')



ax1.legend()
# add 'set_'
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')


ax2.legend()
# add 'set_'
ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')


fig1.savefig('fig1.png')
fig2.savefig('fig2.png')

plt.tight_layout()
plt.show()