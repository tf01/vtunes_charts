# %% import
import numpy as np
import pandas as p
import matplotlib.pyplot as plt

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
data_stack = data.stack(dropna=True)
data_stack.name = 'Person'
write_to_file('data-all.html', data_stack.to_frame().describe().to_html())

# %% sorted line graph of all scores
data_stack_sorted = data_stack.sort_values()
ax = data_stack_sorted.plot(figsize=(15, 15), label='Sorted scores')
# https://stackoverflow.com/questions/37234163/how-to-add-a-line-of-best-fit-to-scatter-plot
# estimate first degree polynomial
xvals = range(len(data_stack_sorted))
z = np.polyfit(xvals, data_stack_sorted, deg=1)
p1 = np.poly1d(z)
z2 = np.polyfit(xvals, data_stack_sorted, deg=2)
p2 = np.polyval(z2, xvals)
z3 = np.polyfit(xvals, data_stack_sorted, deg=3)
p3 = np.polyval(z3, xvals)
z3 = np.polyfit(xvals, data_stack_sorted, deg=3)
p3 = np.polyval(z3, xvals)
# zexp = np.polyfit(xvals, np.log(data_stack_sorted), deg=1)
# pexp = np.polyval(zexp, xvals)
zexpw = np.polyfit(xvals, data_stack_sorted, deg=1, w=np.sqrt(data_stack_sorted))
pexpw = np.polyval(zexpw, xvals)

# ax.axline((0, z[1]), slope=z[0], c='red', linestyle='--', label='1st degree polnomial fit')
ax.plot(xvals, p1(xvals), c='red', linestyle='--', alpha=0.6, label='1st degree polynomial fit')
ax.plot(xvals, p2, c='green', linestyle='--', alpha=0.4, label='2nd degree polynomial fit')
ax.plot(xvals, p3, c='orange', linestyle='--', alpha=0.4, label='3rd degree polynomial fit')
# ax.plot(xvals, pexpw, c='orange', linestyle='--', label='logarithmic fit')
ax.plot(xvals, pexpw, c='blue', linestyle='--', alpha=0.8, label='weighted logarithmic fit')

ax.set_xlabel('(Song, Judge)')
ax.set_ylabel('Score')
ax.set_title('Scores w/ regression lines')
ax.legend()
ax.figure.savefig('linear-plot-reg.png', bbox_inches='tight')

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
ax.hlines(8.0, 1, len(data.columns), colors=['red'], linestyles=':', label='Axe murder cutoff')
ax.set_title('RC Server \'Specter\' Album Score Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Judges')
ax.legend()
ax.figure.savefig('box-person.png', bbox_inches='tight')

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
ax.figure.savefig('box-songs.png', bbox_inches='tight')

# %% stacked data boxplot
ax = data_stack.to_frame().boxplot(figsize=(15, 15), return_type='axes', showmeans=True)
ax.set_title('RC Server \'Specter\' Entire Dataset Boxplot')
ax.set_ylabel('Score')
ax.set_xlabel('Dataset')
ax.figure.savefig('box-all.png', bbox_inches='tight')

# %% description boxplots
ddtp = data_description.transpose()
ddtp.drop(['count', 'std'], inplace=True, axis='columns')
ax = ddtp.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \'Specter\' Data Description Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Metrics')
ax.figure.savefig('box-desc-person.png', bbox_inches='tight')

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
ax.figure.savefig('box-desc-songs.png', bbox_inches='tight')

# %% Load old data
data_old = p.read_csv('specter-preRC.csv', index_col="Song")

# %% Michizure before/after comparison
michi = data.loc['Michizure']
michi_old = data_old.loc['Michizure'].rename('Michizure (previous)')

combined = p.concat([michi_old.to_frame(), michi.to_frame()], axis=1)

ax = combined.plot(figsize=(15, 15), kind='bar', rot=45)
ax.hlines(9.0, -1, len(combined), colors=['purple'], linestyles=':', label='RC Hitlist Threshold')
ax.set_title('Michizure Score Comparison')
ax.set_ylabel('Scores')
ax.set_xlabel('Judges')
ax.legend()
ax.figure.savefig('michi-comparison.png', bbox_inches='tight')
# %% Michi Delta
michi = data.loc['Michizure'].rename('m')
michi_old = data_old.loc['Michizure'].rename('mp')

con = p.concat([michi_old.to_frame(), michi.to_frame()], axis=1)
combined = (michi - michi_old).to_frame()

ax = combined.plot(figsize=(15, 15), kind='bar', rot=45, legend=False)
ax.hlines(0, -1, len(combined), colors=['black'], linestyles='-', linewidth=1)
ax.set_title('Michizure Delta Chart')
ax.set_ylabel('Score Delta')
ax.set_xlabel('Judges')
ax.figure.savefig('michi-delta.png', bbox_inches='tight')

# %% DB before/after comparison
db = data.loc['debutante ball']
db_old = data_old.loc['debutante ball'].rename('debutante ball (previous)')

combined = p.concat([db_old.to_frame(), db.to_frame()], axis=1)
 
ax = combined.plot(figsize=(15, 15), kind='bar', rot=45)
ax.set_title('Debutante Ball Score Comparison')
ax.set_ylabel('Scores')
ax.set_xlabel('Judges')
ax.figure.savefig('db-comparison.png', bbox_inches='tight')

# %% DB Delta
db = data.loc['debutante ball'].rename('db')
db_old = data_old.loc['debutante ball'].rename('db_old')

con = p.concat([db_old.to_frame(), db.to_frame()], axis=1)
combined = (con['db'] - con['db_old'])

ax = combined.plot(figsize=(15, 15), kind='bar', rot=45, legend=False)
ax.hlines(0, -1, len(combined), colors=['black'], linestyles='-', linewidth=1)
ax.set_title('Debutante Ball Delta Chart')
ax.set_ylabel('Score Delta')
ax.set_xlabel('Judges')
ax.figure.savefig('db-delta.png', bbox_inches='tight')

# %% Generate Delta for all songs/people
# data_stack exists, now just have to do data_stack all
data_old_stack = data_old.stack(dropna=True)
data_old_stack.name = 'Old Score'
data_stack.name = 'Current Score'

con_stack = p.concat([data_stack.to_frame(), data_old_stack.to_frame()], axis=1)
con_stack_filtered = con_stack[ (con_stack['Current Score'] != con_stack['Old Score']) ].dropna()
# %% All Changes before/after comparison
ax = con_stack_filtered.plot(figsize=(15, 15), kind='barh')
ax.set_title('All New Score Comparison')
ax.set_ylabel('Scores')
ax.set_xlabel('Judges')
ax.figure.savefig('all-comparison.png', bbox_inches='tight')

# %% All Delta
con_stack_delta = (con_stack_filtered['Current Score'] - con_stack_filtered['Old Score'])
ax = con_stack_delta.plot(figsize=(15, 15), kind='barh', legend=False)
for i in np.arange(-3.5, 2, 0.5):
    ax.vlines(i, -1, len(con_stack_filtered), colors=['black'], linestyles=('-' if i==0 else '--'), linewidth=1)
ax.set_title('All Delta Chart')
ax.set_ylabel('Score Delta')
ax.set_xlabel('Judges')
ax.figure.savefig('all-delta.png', bbox_inches='tight')

# %%
