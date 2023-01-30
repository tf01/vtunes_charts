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
data_description = data.describe()
data.describe()

# %% for info per song
data_songs = data.transpose()
data_songs_description = data_songs.describe()
data_songs.describe()

# %% for info on entire album, collapse into a single column
data_stack = data.stack(dropna=True)
data_stack.describe()

# %% extract means for boxplots
# %% histograms
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
ax = data.hist(figsize=(20, 20), sharey=True, sharex=True)
ax[0][0].get_figure().savefig('hist.png')

# %% histogram of songs
ax = data_songs.hist(figsize=(15, 15), sharey=True, sharex=True)
ax[0][0].figure.savefig('hist-songs.png')

# %% histogram of everything
ax = data_stack.hist(figsize=(10, 10))
ax.figure.savefig('hist-all.png')

# %% boxplots
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot
ax = data.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.hlines(8.0, 1, len(data.columns), colors=['red'], linestyles='dotted', label='Axe murder cutoff')
ax.set_title('RC Server \'Specter\' Album Score Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Judges')
ax.legend()
ax.figure.savefig('box-person.png')

# # %%
# ax = data.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True, whis=(0, 100))
# ax.set_title('RC Server \'Specter\' Album Score Boxplots (including outliers)')
# ax.set_ylabel('Scores')
# ax.set_xlabel('Judges')
# ax.figure.savefig('box-person.png')

# %% Transpose data and make new boxplot
# https://note.nkmk.me/en/python-pandas-t-transpose/
ax = data_songs.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \'Specter\' Song Score Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Songs')
ax.figure.savefig('box-songs.png')

# %% stacked data boxplot
ax = data_stack.to_frame().boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \'Specter\' Entire Dataset Boxplot')
ax.set_ylabel('Score')
ax.set_xlabel('Dataset')
ax.figure.savefig('box-all.png')

# %% description boxplots
ddtp = data_description.transpose()
ddtp.drop(['count', 'std'], inplace=True, axis='columns')
ax = ddtp.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \'Specter\' Data Description Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Metrics')
ax.figure.savefig('box-desc-person.png')

# # %% description normal plots with labels
# ax = ddtp.plot.line(figsize=(15, 15), rot=45)
# ax.set_title('RC Server \'Specter\' Data Description ???')
# ax.set_ylabel('Scores')
# ax.set_xlabel('Metrics')
# ax.set_xticklabels(ddtp.columns.tolist())
# %% song description boxplots
dsdtp = data_songs_description.transpose()
dsdtp.drop(['count', 'std'], inplace=True, axis='columns')
ax = dsdtp.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \'Specter\' Data Song Description Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Metrics')
ax.figure.savefig('box-desc-songs.png')

# %%
