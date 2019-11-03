import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM

def read_poly(file):
    """
    Read a single polygon, 
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
    coordinates = []
    polygons = {}

    for line in lines:
        if line[0] == '#': # is_comment
            pass

        if line == '\n' or line == '': # if empty (is_dataset = False)
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
                else:
                    coordinate = line[1:-2].split(', ')
                    coordinates.append([float(i) for i in coordinate])
                
    return polygons


def plot_polygons(polygons):
    """
    Take a dict whose keys are names for polygons
    and values are arrays of the relevant polygons's coordinates,
    output a graph of those polygons
    """
    for coordinate in polygons.values():
        x = coordinate[:, 0]
        y = coordinate[:, 1]
        plt.plot(x, y)
    
    plt.xlabel('easting')
    plt.ylabel('northing')
    plt.title('Edinburgh - natural neibourhoods')

    return plt

polygons = read_multipoly('natural_neighbourhoods.dat')
plot = plot_polygons(polygons)
plot.show()