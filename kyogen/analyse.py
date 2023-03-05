# %% import
import numpy as np
import pandas as p
import matplotlib as plt

# configure
p.set_option('display.float_format', lambda x: '%.2f' % x)
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# simple save to file

def write_to_file(filename, contents):
    file = open(filename, 'w')
    file.write(contents)
    file.close()

# %% data
data = p.read_csv('kyogen.csv', index_col="Song")
write_to_file('raw-data.html', data.head(20).to_html())

# %%
data_description = data.describe()
write_to_file('data-desc.html', data_description.to_html())

# %%
data_songs = data.transpose()
data_songs_description = data_songs.describe()
write_to_file('data-songs-desc.html', data_songs_description.to_html())

# %%
data_stack = data.stack(dropna=True)
data_stack.name = 'Person'
write_to_file('data-all.html', data_stack.to_frame().describe().to_html())


# copied from specter ver
# %% histograms
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
ax = data.hist(figsize=(20, 20), sharey=True, sharex=True)
ax[0][0].get_figure().savefig('hist-person.png', bbox_inches='tight')

# %% histogram of songs
ax = data_songs.hist(figsize=(15, 15), sharey=True, sharex=True)
ax[0][0].figure.savefig('hist-songs.png', bbox_inches='tight')

# %% histogram of everything
ax = data_stack.hist(figsize=(10, 10))
ax.figure.savefig('hist-all.png', bbox_inches='tight')

# %% boxplots
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot
ax = data.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
# ax.hlines(8.0, 1, len(data.columns), colors=['red'], linestyles=':', label='Axe murder cutoff')
ax.set_title('RC Server \'Kyogen\' Album Score Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Judges')
ax.legend()
ax.figure.savefig('box-person.png', bbox_inches='tight')

# %% Transpose data and make new boxplot
# https://note.nkmk.me/en/python-pandas-t-transpose/
ax = data_songs.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \'Kyogen\' Song Score Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Songs')
ax.figure.savefig('box-songs.png', bbox_inches='tight')

# %% stacked data boxplot
ax = data_stack.to_frame().boxplot(figsize=(15, 15), return_type='axes', showmeans=True)
ax.set_title('RC Server \'Kyogen\' Entire Dataset Boxplot')
ax.set_ylabel('Score')
ax.set_xlabel('Dataset')
ax.figure.savefig('box-all.png', bbox_inches='tight')

# %% description boxplots
ddtp = data_description.transpose()
ddtp.drop(['count', 'std'], inplace=True, axis='columns')
ax = ddtp.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \'Kyogen\' Data Description Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Metrics')
ax.figure.savefig('box-desc-person.png', bbox_inches='tight')

# %% song description boxplots
dsdtp = data_songs_description.transpose()
dsdtp.drop(['count', 'std'], inplace=True, axis='columns')
ax = dsdtp.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \'Kyogen\' Data Song Description Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Metrics')
ax.figure.savefig('box-desc-songs.png', bbox_inches='tight')
# %%
