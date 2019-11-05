import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM

def read_poly(file):
    """
    Read a file contains the coordinates of a single polygon,
    return an array of the polygon's coordinates.
    """
    poly = open(file).readlines()
    coordinates = []
    for line in poly:
        if line != '\n' and line != '':
            line = line[1:-2].split(', ')
            coordinates.append([float(i) for i in line])
    return np.asarray(coordinates)


def read_multipoly(file):
    """
    Read multi-polygon file, 
    return a dict whose keys are names of polygons 
    and values are arrays of the relevant polygons' coordinates.
    """
    multipoly = open(file)
    lines = multipoly.readlines()
    coordinates = [] # a list temporarily saves coordinates of each polygons
    polygons = {} # a dict, names of places as keys, relevant coordinates arrays as values

    for line in lines:
        if line[0] == '#': # is comment
            pass

        if line == '\n' or line == '': # if empty (is_dataset = False), save coordinates into a dict
            polygons[name] = np.asarray(coordinates)
            coordinates = [] # reset coordinates
        else:
            if line[0] != '(' and line[0] != '[': # if not coordinate
                name = line[:-1] # ignore "\n"
            else:
                if line[0] == '[':
                    line = line[2:-3].split('), (')
                    for coordinate in line:
                        coordinate = coordinate.split(', ')
                        coordinates.append([float(i) for i in coordinate])
                elif line[0] == '(':
                    coordinate = line[1:-2].split(', ')
                    coordinates.append([float(i) for i in coordinate])
                else:
                    raise ValueError('Wrong coordinate format!')
                
    return polygons


def plot_polygons(polygons):
    """
    Take a dict whose keys are names for polygons
    and values are arrays of the relevant polygons's coordinates,
    output a graph of those polygons
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for name, coordinate in polygons.items():
        ax.add_patch(plt.Polygon(coordinate, fill=False, label=name))
    
    ax.set_title('Edinburgh - natural neibourhoods')
    ax.set_xlim(309000, 334000) # ref: https://stackoverflow.com/questions/3777861/setting-y-axis-limit-in-matplotlib
    ax.set_ylim(657500, 680000)
    ax.set_xlabel('easting')
    ax.set_ylabel('northing')

    return fig

if __name__ == '__main__':
    polygons = read_multipoly('./ReadNPlot/data/natural_neighbourhoods.dat')
    plot = plot_polygons(polygons)
    plot.show()