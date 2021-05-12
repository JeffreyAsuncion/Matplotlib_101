import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates


plt.style.use('seaborn')

data = pd.read_csv('data4.csv')

# convert string to datetime
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']


plt.plot_date(price_date, price_close, linestyle='solid')

# GetCurrentFigure
plt.gcf().autofmt_xdate()

date_format = mpl_dates.DateFormatter('%b, %d %Y')

# GetCurrentAccess
plt.gca().xaxis.set_major_formatter(date_format)


plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()  # this adds padding for presentation on smaller screens

plt.show()