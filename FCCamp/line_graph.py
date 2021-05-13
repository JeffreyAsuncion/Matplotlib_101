import pandas as pd
import matplotlib.pyplot as plt


gas = pd.read_csv('gas_prices.csv')

# plt.plot(gas.Year, gas.USA, 'r.-', label='USA')
# plt.plot(gas.Year, gas.Canada, 'b.-', label='Canada')
# plt.plot(gas['Year'], gas['South Korea'], 'g.-', label='South Korea')

# # This is for all the data
# for country in gas:
#     if country != 'Year':
#         plt.plot(gas.Year, gas[country],  '.-', label=f'{country}')

country_to_look_at = ['Australia', 'USA', 'Canada', 'South Korea']

for country in gas:
    if country != 'Year':
        if country in country_to_look_at:
            plt.plot(gas.Year, gas[country],  '.-', label=f'{country}')

plt.title('USA vs Cananda Gas Prices', fontdict={'fontweight':'bold', 'fontsize':18})

plt.xticks(gas.Year[::3].tolist()+[2011])

plt.ylabel('Dollars/Gallon')
plt.xlabel('Year')

plt.legend(loc='upper left')

plt.savefig('GasPriceFigure.png', dpi=300)

plt.show()