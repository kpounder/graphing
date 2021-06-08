# This file gives several examples. 

import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import graphing.custom_seaborn as csns


# Sample data for graphs 
temp_data = pd.DataFrame(
    data={
        'cels': np.arange(0, 110, step=10),
    }
)
temp_data['fahr'] = 9/5 * temp_data['cels'] + 32 
l = len(pd.date_range(start=datetime.date(2018,1,1), end=datetime.date(2018,7,1), freq='D'))
test_data = pd.DataFrame(
    data={
        'x': np.arange(1, l+1, step=1),
        'y': 1/(2*l) * np.arange(1, l+1, step=1),
        'd': pd.date_range(start=datetime.date(2018,1,1), end=datetime.date(2018,7,1), freq='D'),
        'z': np.exp(-1*np.arange(1, l+1, step=1)),
        'a': 5/(l) * np.arange(1, l+1, step=1)
    }
)


# Basic line plot
fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(
    x='cels', y='fahr', data=temp_data, err_style=None, linewidth=5, ax=ax
)
ax = csns.customize_axis(
    ax=ax,
    title='Relationship between Temperatures in Fahrenheit and Celsius',
    xlabel='Degrees Celsius',
    ylabel='Degrees Fahrenheit'
)
plt.show()

# Line plot with custom x axis label, ticks, and tick marks 
fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(
    x='d', y='y', data=test_data, err_style=None, linewidth=5, ax=ax
)
ax = csns.customize_axis(
    ax=ax,
    grid=True,
    xlabel='Date (Quarter)',
    xticks=pd.date_range(start=datetime.date(2018,1,1), end=datetime.date(2018,7,1), freq='QS'),
    xticklabels=pd.date_range(start=datetime.date(2018,1,1), end=datetime.date(2018,7,1), freq='QS').map(lambda dt: dt.strftime('%b %y'))
)
plt.show()

# Scatter plot 
fig, ax = plt.subplots(figsize=(10,5))
sns.scatterplot(
    x='x', y='a', data=test_data.iloc[:5, :], ax=ax
)
ax = csns.customize_axis(
    ax=ax,
    title='My Title',
    xlabel='X Axis Label',
    ylabel='Y Axis Label',
    xticks=np.arange(1, 6, step=1),
    yticks=np.arange(0, 1.1, step=0.1),
    xticklabels=[1, 2, 3, 4, 5], #['One', 'Two', 'Three', 'Four', 'Five'],
    yticklabels=[f"{100*y:0.1f}%" for y in np.arange(0, 1.1, step=0.1)],
    spines={'top': False, 'right': False, 'bottom': 'grey', 'left': 'grey'}
)
plt.show()

# Two stacked graphs (subplots)
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10,8), gridspec_kw={'height_ratios': [1, 3], 'hspace': 0.15})
sns.lineplot(
    x='x', y='y', data=test_data, color='grey', err_style=None, linewidth=3, ax=ax[0]
)
sns.lineplot(
    x='x', y='z', data=test_data, color='steelblue', err_style=None, linewidth=5, ax=ax[1]
)
ax[0] = csns.customize_axis(
    ax=ax[0],
    grid=True,
    title='Overall Title',
    ylabel='Upper Y Title',
    showylabel=True,
    showxlabel=False,
    spines={'top': False, 'right': False, 'bottom': False, 'left': 'grey'}
)
ax[1] = csns.customize_axis(
    ax=ax[1],
    grid=True,
    ylabel='Lower Y Title',
    xlabel='X Title'
)
plt.show()

# Bar plot 
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(
    x='d', y='z', data=test_data.iloc[:5, :], color='lightgrey', ax=ax
)
ax = csns.customize_axis(
    ax=ax,
    xticklabels=['Mon', 'Tues', 'Weds', 'Thurs', 'Fri'],
    spines={'top': False, 'right': False, 'bottom': 'grey', 'left': False}
)
ax.patches[0].set_color('steelblue')
ax.patches[-1].set_color('salmon')
plt.show()

# Overlayed histograms 
fig, ax = plt.subplots(figsize=(10,8))
sns.distplot(
    a=test_data['z'], bins=20, kde=False, norm_hist=False, color='grey', label='Control', ax=ax
)
sns.distplot(
    a=test_data['y'], bins=20, kde=False, norm_hist=False, color='steelblue', label='Test', hist_kws=dict(alpha=0.25), ax=ax
)
ax = csns.customize_axis(
    ax=ax,
    legend=True
)
plt.show()
