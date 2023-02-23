# %% Build the page
import os

# create md file
output = open('../specter.md', 'w')

# add styles
output.write('''<style>
  .plot_figure {
    max-width: 100vw;
    width: 200%;
  }
</style>
# Specter
Here are the results for Hoshimachi Suisei's *Specter*!

Thanks to all of the participants! This was fun to set up, so hopefully we can do this with more albums in the future.
''')

output.write('''

# Raw Scores

''')
htmlfile = open('raw-data.html', 'r')
output.writelines(htmlfile.readlines())


output.write('''

# Data Description

## Person-wise

''')
htmlfile = open('data-desc.html', 'r')
output.writelines(htmlfile.readlines())

output.write('''

<img class="plot_figure" src="specter/box-desc-person.png"/>

## Song-wise

''')
htmlfile = open('data-songs-desc.html', 'r')
output.writelines(htmlfile.readlines())

output.write('''

<img class="plot_figure" src="specter/box-desc-songs.png"/>

## Entire dataset

''')
htmlfile = open('data-all.html', 'r')
output.writelines(htmlfile.readlines())

output.write('''

### Regressions
Good shout on this one Red. It was  interesting to align all of the scores and try and fit some lines to 'em
<img class="plot_figure" src="specter/linear-plot-reg.png"/>

# Boxplots
Here is *Tommy's quick guide to box and whisker plots*:
- Top and bottom horizontal lines represent the min and max values
  - Also known as *whiskers*
- Green horizontal line is the median
- Horizontal lines that are the top and bottom edges of the box are the medians of the top and bottom 50% of the data respectively
- Green triangle is the mean
- Circles are outliers
  - A point is classified as an outlier (in this case) if they are further than 1.5x the interquartile range away from the box edge
  - The interquartile range is the difference between the medians of the top and bottom 50% of the data
    - AKA, the vertical length of the box!
- Segments separated by horizontal lines represent 25% of the dataset
  - e.g. if the bottom whisker is at 6, and the bottom edge of the box is at 7.5, 25% of the data has a value between 6 and 7.5
  - Therefore, the entire 'box' is the middle 50% of the data!
- If your scores are below the red line, you're dead
  - o7
- If your scores are *above* the purple line, you're dead
  - o7
## Person-wise
<img class="plot_figure" src="specter/box-person.png"/>

## Song-wise
<img class="plot_figure" src="specter/box-songs.png"/>

## Entire dataset
<img class="plot_figure" src="specter/box-all.png"/>

# Histograms

## Person-wise
<img class="plot_figure" src="specter/hist-person.png"/>

## Song-wise
<img class="plot_figure" src="specter/hist-songs.png"/>

## Entire dataset
<img class="plot_figure" src="specter/hist-all.png"/>

# First Impressions vs Rescore

I've still got the old scores, so here are some comparisons:

## Michizure

<img class="plot_figure" src="specter/michi-comparison.png"/>

<img class="plot_figure" src="specter/michi-delta.png"/>

## Debutante Ball

<img class="plot_figure" src="specter/db-comparison.png"/>

<img class="plot_figure" src="specter/db-delta.png"/>

''')
# close file
output.close()
# %%
