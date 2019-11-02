import numpy as np
from matplotlib import pyplot as plt

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
    group = []
    groups = []

    # Group by different polygons
    for line in lines:
        if line[0] == '#': # is comment
            pass
        elif line[0] == '' or line[0] == '\n': # is_dataset = False
            groups.append(group)
            group = []
            pass
        else:
            if line[0] == '[':
                line = line[2:-3].split('), (')
                for coordinate in line:
                    group.append(coordinate)
            elif line[0] == '(':
                group.append(line[1:-2])
            else: # is_name
                group.append(line[:-1])
    
    # Put groups into dict
    for group in groups:
        for coordinate in group[1:]:
            coordinate = [float(i) for i in coordinate.split(', ')]
        polygons[group[0]] = group[1:]
    
    return polygons

    '''
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
    '''


def plot_polygons(polygons):
    """
    Take a dict whose keys are names for polygons
    and values are arrays of the relevant polygons's coordinates,
    output a graph of those polygons
    """
    

polygons = read_multipoly('natural_neighbourhoods.dat')