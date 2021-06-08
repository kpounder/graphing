import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import graphing.custom_seaborn as csns


l = len(pd.date_range(start=datetime.date(2018,1,1), end=datetime.date(2018,7,1), freq='D'))
test_data = pd.DataFrame(
    data={
        'x': np.arange(1, l+1, step=1),
        'y': 1/(2*l) * np.arange(1, l+1, step=1),
        'd': pd.date_range(start=datetime.date(2018,1,1), end=datetime.date(2018,7,1), freq='D'),
        'z': np.exp(-1*np.arange(1, l+1, step=1))
    }
)

fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(
    x='x', y='y', data=test_data.iloc[:5, :], err_style=None, linewidth=5, ax=ax
)
ax = csns.customize_axis(
    ax=ax
)
plt.show()

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

fig, ax = plt.subplots(figsize=(10,5))
sns.scatterplot(
    x='x', y='y', data=test_data.iloc[:10, :], ax=ax
)
ax = csns.customize_axis(
    ax=ax,
    title='My Title',
    xlabel='X Axis Label',
    ylabel='Y Axis Label',
    xticks=np.arange(1, 6, step=1),
    yticks=np.arange(0, 1.1, step=0.1),
    xticklabels=['One', 'Two', 'Three', 'Four', 'Five'],
    yticklabels=[f"{100*y:0.1f}%" for y in np.arange(0, 1.1, step=0.1)],
    spines={'top': False, 'right': False, 'bottom': 'grey', 'left': 'grey'}
)
plt.show()

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
    ylabel='Upper Y Axis Title',
    showylabel=True,
    showxlabel=False,
    spines={'top': False, 'right': False, 'bottom': False, 'left': 'grey'}
)
ax[1] = csns.customize_axis(
    ax=ax[1],
    grid=True,
    ylabel='Lower Y Axis Title'
)
plt.show()

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(
    x='d', y='z', data=test_data.iloc[:5, :], color='lightgrey', ax=ax
)
ax = csns.customize_axis(
    ax=ax,
    grid=True,
    xticklabels=['Mon', 'Tues', 'Weds', 'Thurs', 'Fri'],
    spines={'top': False, 'right': False, 'bottom': 'grey', 'left': False}
)
ax.patches[0].set_color('steelblue')
ax.patches[-1].set_color('salmon')
plt.show()


fig, ax = plt.subplots(figsize=(10,8))
sns.distplot(
    a=test_data['z'], bins=10, kde=False, norm_hist=False, color='grey', label='Control', ax=ax
)
sns.distplot(
    a=test_data['y'], bins=10, kde=False, norm_hist=False, color='steelblue', label='Test', hist_kws=dict(alpha=0.25), ax=ax
)
ax = csns.customize_axis(
    ax=ax,
    legend=True
)
plt.show()
