import pandas as pd
import matplotlib.pyplot as plt
from functions import state_list
from matplotlib import style
style.use('fivethirtyeight')
import quandl as Quandl
api_key = open('apiKey.txt', 'r').read()

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

bridge_height = {
    'meters':
    [10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]
}
df = pd.DataFrame(bridge_height)

# tring to figure out the erronous data
df['std'] = pd.rolling_std(df['meters'], 2)
# finding the avarage std
df_std = df.describe()['meters']['std']
print(df_std)
# choosing cases in which the std of the data is smaller than the avarage std
df = df[(df['std'] < df_std)]
print(df)

df['meters'].plot()
plt.show()