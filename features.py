import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import pandas as pd

def data_analysis(df, fields, targets):
    # source: https://towardsdatascience.com/exploratory-data-analysis-eda-visualization-using-pandas-ca5a04271607
    # print(df.head())
    # describe(df, fields)
    # boxplot(df, fields)
    # histogram(df, fields, titles)
    # correlation(df, fields, targets)
    scatter(df, fields, targets)
    # scatter_overlay(df, fields, targets)


def scatter(df, features, targets):

    for target in targets:
        fig = plt.figure()
        colors = get_colors()
        markers = get_markers()
        ax = df.plot(kind='scatter', x=features[0], y=target, color=colors[0], marker=markers[0],
                     label=features[0])
        for f, c, m in zip(features[1:], colors[1:], markers[1:]):
            df.plot(kind='scatter', x=f, y=target, color=c, marker=m, label=f, ax=ax)

        plt.legend(loc='center right')
        plt.tight_layout()
        plt.show()


def correlation(df, fields, targets):
    corr = df.corr()[targets].ix[fields]
    corr.style.background_gradient(cmap='coolwarm').set_precision(2)
    # plot the heatmap
    # sns.heatmap(corr,
    #             xticklabels=corr.columns,
    #             yticklabels=corr.columns)
    ax = sns.heatmap(
        corr,
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True
    )
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
    )
    plt.show()


def histogram(df, fields, titles):
    df[fields].plot.hist(title=titles[0])
    plt.show()


def boxplot(df, fields, type='h'):
    if type == 'h':
        # horizontal boxplot
        df[fields].plot.box(vert=False, grid=True)
    else:
        # vertical boxplot
        df[fields].plot.box()
    plt.show()


def describe(df, fields):
    print(df[fields].describe())


def get_colors():
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

    # Sort colors by hue, saturation, value and name.
    by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                    for name, color in colors.items())
    sorted_names = [name for hsv, name in by_hsv]
    print(sorted_names.reverse())
    return sorted_names

def get_markers():
    # markers = [m for m, func in Line2D.markers.items()
    #                     if func != 'nothing' and m not in Line2D.filled_markers]
    markers = ['.', '+', 'x', '2', '*', 'P', 'X', 's', 'd', 'D', 'v', '^', '>']
    return markers