from matplotlib import pyplot as plt
import numpy as np



def plot(x_values, satellites, plot_method):
    plt.plot(x_values, np.array(list(map(plot_method, satellites))))
    plt.show()