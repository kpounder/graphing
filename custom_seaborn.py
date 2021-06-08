import seaborn as sns
import yaml


with open('/Users/kpounder/Documents/code/graphing/preferences.yaml') as file:
    PREFS = yaml.load(file, Loader=yaml.FullLoader)


def customize_axis(
    ax,
    grid=False,
    title='',
    xlabel='',
    ylabel='',
    showxlabel=True,
    showylabel=True,
    xticks=None,
    yticks=None,
    xticklabels=None,
    yticklabels=None,
    spines={'top': False, 'right': False, 'bottom': 'grey', 'left': 'grey'},
    legend=False
):
    if grid:
        ax.grid(axis='both', **PREFS['grid'])
    else:
        ax.grid(False)

    if title:
        ax.set_title(title, **PREFS['title'])

    ax.set_xlabel(xlabel, **PREFS['axislabels'], **PREFS['xaxislabel'])
    ax.set_ylabel(ylabel, **PREFS['axislabels'], **PREFS['yaxislabel'])

    if xticks is not None:
        ax.set_xticks(xticks)
    if yticks is not None:
        ax.set_yticks(yticks)
    if xticklabels is not None:
        ax.set_xticklabels(xticklabels)
    if yticklabels is not None:
        ax.set_yticklabels(yticklabels)

    if showxlabel and showylabel:
        ax.tick_params(axis='both', **PREFS['axisticks'])
    elif showylabel and (not showxlabel):
        ax.tick_params(axis='x', bottom=False, labelbottom=False, **PREFS['axisticks'])
        ax.tick_params(axis='y', **PREFS['axisticks'])

    for side in spines.keys():
        if type(spines[side]) == str:
            ax.spines[side].set_color(spines[side])
        else:
            ax.spines[side].set_visible(spines[side])

    if legend:
        ax.legend()
        l = ax.get_legend()
        for text in l.get_texts():
            text.set_color('grey')

    return ax
