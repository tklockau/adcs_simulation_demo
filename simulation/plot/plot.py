from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from .graph import Graph

def plot(x_values, graphs: Graph or list[Graph], x_label: str="", y_label: str="", title: str=""):
    
    figure, plot = _plot_graphs(x_values, _make_graphs_list(graphs))
    plot = _set_up_text(plot, x_label, y_label, title)
    figure, plot = _set_plot_style(figure, plot)

    plt.show()

def _make_graphs_list(graphs: Graph or list[Graph]) -> list[Graph]:
    if type(graphs) != list:
        graphs = [graphs]

    return graphs

def _plot_graphs(x_values, graphs) -> tuple[Figure, Axes]:
    figure, plot = plt.subplots()

    for graph in graphs:
        plot.plot(x_values, graph.y_values, label=graph.label, color=graph.color)

    return figure, plot

def _set_up_text(plot: Axes, x_label: str, y_label: str, title: str):
    plot.legend()
    plot.set_xlabel(x_label)
    plot.set_ylabel(y_label)
    plot.set_title(title)

    return plot

def _set_plot_style(figure: Figure, plot: Axes) -> tuple[Figure, Axes]:
    plt.style.use('dark_background')
    background_color = "#1d1e1e"

    plot.set_facecolor(background_color)
    figure.set_facecolor(background_color)
    plot.legend().get_frame().set_facecolor(background_color)

    return figure, plot