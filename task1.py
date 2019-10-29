import numpy as np
import matplotlib.pyplot as plt

def read_plenty(file):
    """
    Take the given plenty.data file and output an narray.
    """
    plenty = open(file)
    lines = plenty.readlines()
    dataframe = []
    for line in lines:
        line = line.split(' ')
        dataframe.append([float(i) for i in line])
    return np.asarray(dataframe)


# Plotting
def plot_plenty(plenty_array):
    x = plenty_array[:, 0] # the first column. ref:https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html
    for column in range(1, np.size(plenty_array,1)): # loop from the first column to the last. ref:https://docs.scipy.org/doc/numpy/reference/generated/numpy.ma.size.html
        y = plenty_array[:, column]
        plt.plot(x, y)
    return plt

# main
plenty_array = read_plenty("./plenty.data")
plenty_plt = plot_plenty(plenty_array)
plenty_plt.show()