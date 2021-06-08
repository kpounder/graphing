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
    """This function customizes the provided Matplotlib Axis object. 

    Parameters:
    ax: Matplotlib Axis object
    grid: bool 
        If True, graph will include grid. 
    title: str 
        The title of the graph (if provided). 
    xlabel: str
        The label on the x-axis of the graph (if provided).
    ylabel: str 
        The label on the y-axis of the graph (if provided). 
    showxlabel: bool
        If True, the x-axis label will be displayed. 
    showylabel: bool
        If True, the y-axis label will be displayed.
    xticks: list 
        The location of tick marks on the x-axis (if provided).
    yticks: list 
        The location of tick marks on the y-axis (if provided). 
    xticklabels: list
        The labels for the x-ticks (if provided). 
    yticklabels: list
        The labels for the y-ticks (if provided). 
    spines: dict 
        For each edge of the graph (top/bottom/left/right), whether to draw a border
        and if so, the border color. 
    legend: bool
        If True, the legend will be displayed. 
    
    Returns:
    ax: Matplotlib Axis object 

    Example: 
    ax = customize_axis(ax, title='My Graph Title', xlabel='My X-Axis Label')
    """

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
