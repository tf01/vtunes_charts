
# %% import
import numpy as np
import pandas as p
import matplotlib.pyplot as plt

# %% get data
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
data = p.read_csv('specter.csv', index_col="Song")
data.head(20)

# %%
# drop if required
# dropping = ["Saph"]
# data = data.drop(labels=dropping, axis='columns')
# %% Describe the data
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
p.set_option('display.float_format', lambda x: '%.2f' % x)
data.describe()

# %% for info per song
data_songs = data.transpose()
data_songs.describe()

# %% for info on entire album, collapse into a single column
data_stack = data.stack(dropna=True)
data_stack.describe()
# %%
