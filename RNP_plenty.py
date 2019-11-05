import numpy as np
import matplotlib.pyplot as plt

def read_plenty(file):
    """
    Take the sample plenty.data file in *data* folder and output an array.
    """
    plenty = open(file)
    lines = plenty.readlines()
    dataframe = []
    for line in lines:
        line = line.split(' ')
        dataframe.append([float(i) for i in line])
    return np.asarray(dataframe)


# Plotting
def plot_plenty(array):
    """
    Take the output array from **read_plenty**,
    then use the first column as x values,
    and other columns as y values to plot a graph.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = array[:, 0] # the first column. ref:https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html
    i = 1
    for column in range(1, array.shape[1]): # loop from the first column to the last. ref:https://docs.scipy.org/doc/numpy/reference/generated/numpy.ma.size.html
        y = array[:, column]
        ax.plot(x, y, label='Curve '+str(i))
        i += 1

    ax.set_title('Plenty Data')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend(loc='upper center', ncol=2)

    return fig

if __name__ == '__main__':
    plenty_array = read_plenty("./data/plenty.data")
    plenty_plt = plot_plenty(plenty_array)
    plenty_plt.show()