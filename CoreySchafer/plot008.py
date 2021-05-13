import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

date = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30),
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot_date(date, y, linestyle='solid')

# GetCurrentFigure
plt.gcf().autofmt_xdate()

date_format = mpl_dates.DateFormatter('%b, %d %Y')

# GetCurrentAccess
plt.gca().xaxis.set_major_formatter(date_format)

# data = pd.read_csv('data4.csv')
# price_date = data['Date']
# price_close = data['Close']


# plt.title('Bitcoin Prices')
# plt.xlabel('Date')
# plt.ylabel('Closing Price')

# plt.tight_layout()  # this adds padding for presentation on smaller screens

plt.show()