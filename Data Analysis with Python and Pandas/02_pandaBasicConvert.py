import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

# defining some sample data
web_stats = {
    'Day': [1, 2, 3, 4, 5, 6],
    'Visitors': [43, 34, 65, 56, 29, 76],
    'Bounce_Rate': [65, 67, 78, 65, 45, 52]
}

# converting to a dataframe
df = pd.DataFrame(web_stats)
print(df.head())
# setting an index
df.set_index('Day', inplace=True)
print(df.head())
# refferencing a column
print(df['Bounce_Rate'])
print(df.Visitors)
print(df[['Bounce_Rate', 'Visitors']])
# converting
print(df.Visitors.tolist())
print(np.array(df[['Bounce_Rate', 'Visitors']]))
df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))
print(df2)