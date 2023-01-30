# %% import
import numpy as np
import pandas as p
import matplotlib.pyplot as plt

# configure
p.set_option('display.float_format', lambda x: '%.2f' % x)

# simple save to file

def write_to_file(filename, contents):
    file = open(filename, 'w')
    file.write(contents)
    file.close()

# %% get data
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
data = p.read_csv('specter.csv', index_col="Song")
write_to_file('raw-data.html', data.head(20).to_html())

# %%
# drop if required
# dropping = ["Saph"]
# data = data.drop(labels=dropping, axis='columns')
# %% Describe the data
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
data_description = data.describe()
write_to_file('data-desc.html', data_description.to_html())

# %% for info per song
data_songs = data.transpose()
data_songs_description = data_songs.describe()
write_to_file('data-songs-desc.html', data_songs_description.to_html())

# %% for info on entire album, collapse into a single column
data_stack = data.stack(dropna=True).to_frame()
write_to_file('data-all.html', data_stack.describe().to_html())

# %% histograms
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
ax = data.hist(figsize=(20, 20), sharey=True, sharex=True)
ax[0][0].get_figure().savefig('hist.png')

# %% histogram of songs
ax = data_songs.hist(figsize=(15, 15), sharey=True, sharex=True)
ax[0][0].figure.savefig('hist-songs.png')

# %% histogram of everything
ax = data_stack.hist(figsize=(10, 10))
ax[0][0].figure.savefig('hist-all.png')

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
ax = data_stack.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
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
