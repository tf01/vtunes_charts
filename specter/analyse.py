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
# %% histograms
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
ax = data.hist(figsize=(20, 20), sharey=True, sharex=True)

# %% histogram of songs
ax = data_songs.hist(figsize=(15, 15), sharey=True, sharex=True)

# %% histogram of everything
ax = data_stack.hist(figsize=(10, 10))

# %% boxplots
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot
ax = data.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \'Specter\' Album Score Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Judges')

# %%
ax = data.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True, whis=(0, 100))
ax.set_title('RC Server \'Specter\' Album Score Boxplots (including outliers)')
ax.set_ylabel('Scores')
ax.set_xlabel('Judges')

# %% Transpose data and make new boxplot
# https://note.nkmk.me/en/python-pandas-t-transpose/
ax = data_songs.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \'Specter\' Song Score Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Songs')

# %% stacked data boxplot
ax = data_stack.to_frame().boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \'Specter\' Entire Dataset Boxplot')
ax.set_ylabel('Score')
ax.set_xlabel('Dataset')
# %%
