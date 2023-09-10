# %% import
import numpy as np
import pandas as p
import matplotlib as plt
from scipy.optimize import curve_fit

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
collection_name = 'Blue Journey'
data = p.read_csv('blue_journey.csv', index_col="Song")
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
# zexpw = np.polyfit(xvals, data_stack_sorted, deg=1, w=np.sqrt(data_stack_sorted))
# pexpw = np.polyval(zexpw, xvals)

# # %% curve fit
# popt, pcov = curve_fit(lambda t, a, b, c: a * np.exp(b * t) + c, xvals, data_stack_sorted)
# a = popt[0]
# b = popt[1]
# c = popt[2]
# # x_fitted = np.linspace(np.min(xvals), np.max(xvals), 100)
# y_fitted = a * np.exp(b * xvals) + c


# ax.axline((0, z[1]), slope=z[0], c='red', linestyle='--', label='1st degree polnomial fit')
ax.plot(xvals, p1(xvals), c='red', linestyle='--', alpha=0.6, label='1st degree polynomial fit')
ax.plot(xvals, p2, c='green', linestyle='--', alpha=0.4, label='2nd degree polynomial fit')
ax.plot(xvals, p3, c='orange', linestyle='--', alpha=0.4, label='3rd degree polynomial fit')
# ax.plot(xvals, pexpw, c='orange', linestyle='--', label='logarithmic fit')
# ax.plot(xvals, pexpw, c='blue', linestyle='--', alpha=0.8, label='weighted logarithmic fit')
# ax.plot(xvals, y_fitted, c='blue', linestyle='--', alpha=0.8, label='curve fit')

ax.set_xlabel('(Song, Judge)')
ax.set_ylabel('Score')
ax.set_title('Scores w/ regression lines')
ax.legend()
ax.figure.savefig('linear-plot-reg.png', bbox_inches='tight')


# %% proper 
# %% histograms
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
ax = data.hist(figsize=(20, 20), sharey=True, sharex=True)
ax[0][0].get_figure().savefig('hist-person.png', bbox_inches='tight')

# %% histogram of songs
ax = data_songs.hist(figsize=(15, 15), sharey=True, sharex=True)
ax[0][0].figure.savefig('hist-songs.png', bbox_inches='tight')

# %% histogram of everything
ax = data_stack.hist(figsize=(10, 10))
ax.set_title('RC Server \''+collection_name+'\' Album Dataset Histogram')
ax.set_ylabel('Scores')
ax.legend()
ax.figure.savefig('hist-all.png', bbox_inches='tight')

# %% boxplots
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot
ax = data.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
# ax.hlines(8.0, 1, len(data.columns), colors=['red'], linestyles=':', label='Axe murder cutoff')
ax.set_title('RC Server \''+collection_name+'\' Album Score Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Judges')
ax.legend()
ax.figure.savefig('box-person.png', bbox_inches='tight')

# %% Transpose data and make new boxplot
# https://note.nkmk.me/en/python-pandas-t-transpose/
ax = data_songs.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \''+collection_name+'\' Song Score Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Songs')
ax.figure.savefig('box-songs.png', bbox_inches='tight')

# %% stacked data boxplot
ax = data_stack.to_frame().boxplot(figsize=(15, 15), return_type='axes', showmeans=True)
ax.set_title('RC Server \''+collection_name+'\' Entire Dataset Boxplot')
ax.set_ylabel('Score')
ax.set_xlabel('Dataset')
ax.figure.savefig('box-all.png', bbox_inches='tight')

# %% description boxplots
ddtp = data_description.transpose()
ddtp.drop(['count', 'std'], inplace=True, axis='columns')
ax = ddtp.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \''+collection_name+'\' Data Description Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Metrics')
ax.figure.savefig('box-desc-person.png', bbox_inches='tight')

# %% song description boxplots
dsdtp = data_songs_description.transpose()
dsdtp.drop(['count', 'std'], inplace=True, axis='columns')
ax = dsdtp.boxplot(figsize=(15, 15), return_type='axes', rot=45, showmeans=True)
ax.set_title('RC Server \''+collection_name+'\' Data Song Description Boxplots')
ax.set_ylabel('Scores')
ax.set_xlabel('Metrics')
ax.figure.savefig('box-desc-songs.png', bbox_inches='tight')
# %%
