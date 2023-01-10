"""Code showcasing pyplot and pandas using the wine dataset."""


import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import pandas as pd
import sklearn.datasets


def _plot_hist(data, feature):
    """Plot the histogram of the given feature."""
    hist_fig = plt.figure()
    hist_ax = hist_fig.subplots()
    for curr_label in pd.unique(data["class_label"]):
        data_filtered = data[data["class_label"] == curr_label]
        hist_ax.hist(
            data_filtered.loc[:, feature], alpha=0.5, label="class " + str(curr_label)
        )
        hist_ax.set_xlabel(feature)
        hist_ax.set_ylabel("n")
        hist_ax.legend()
        hist_ax.xaxis.set_major_formatter(tic.PercentFormatter(xmax=100, decimals=1))
        hist_ax.yaxis.set_major_formatter(tic.StrMethodFormatter(fmt="{x:.0f}"))


def _plot_scatter(data, feature):
    """Plot the distribution of all other features against the given feature."""
    scatter_fig = plt.figure()
    scatter_ax = scatter_fig.subplots(nrows=3, ncols=4)
    scatter_ax = scatter_ax.flatten()
    subplot_cnt = 0
    for curr_feature in data.drop(columns="class_label").columns:
        if curr_feature != feature:
            for curr_label in pd.unique(data["class_label"]):
                data_filtered = data[data["class_label"] == curr_label]
                scatter_ax[subplot_cnt].scatter(
                    x=data_filtered.loc[:, curr_feature],
                    y=data_filtered.loc[:, feature],
                    marker="o",
                    label="class " + str(curr_label),
                )
                scatter_ax[subplot_cnt].set_xlabel(curr_feature)
                scatter_ax[subplot_cnt].set_ylabel(feature)
                scatter_ax[subplot_cnt].legend()
            subplot_cnt += 1


def main():
    """Showcase the 'hist' and 'scatter' plots using the wine dataset."""
    wine_dataset = sklearn.datasets.load_wine()
    data = pd.DataFrame(data=wine_dataset["data"])
    data.columns = wine_dataset["feature_names"]
    data["class_label"] = wine_dataset["target"]
    selected_feature = "alcohol"
    _plot_hist(data=data, feature=selected_feature)
    _plot_scatter(data=data, feature=selected_feature)
    plt.show()


if __name__ == "__main__":
    main()
