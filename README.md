# ReadNPlot

🌏*A python package for reading and plotting geographical data*🌏

------------------------------------------------------------

## Modules

#### RNP_plenty.py

**read_plenty**: Take the sample plenty.data file in *data* folder and output an array.

**plot_plenty**: Take the output array from **read_plenty**, then use the first column as x values, and other columns as y values to plot a graph.

#### RNP_polygon.py

**read_poly**: Read a file contains the coordinates of a single polygon, return an array of the polygon's coordinates.

**read_multipoly**: Read multi-polygon file, return a dict whose keys are names of polygons and values are arrays of the relevant polygons' coordinates.

**plot_polygons**: Take a dict whose keys are names for polygons and values are arrays of the relevant polygons's coordinates, output a graph of those polygons

## How to use

1. Put the folder that contains this README file to your working directory
2. Open a terminal in your working directory, and try the samples:

##### On Linux / MacOS

```bash
python3 -i RNP_plenty.py # a sample of RNP_plenty module
python3 -i RNP_polygon.py # a sample of RNP_polygon module
```

##### On Windows

```powershell
python -i RNP_plenty.py # a sample of RNP_plenty module
python -i RNP_polygon.py # a sample of RNP_polygon module
```

--------------------------------------------------

#### Acknowledgement

👍 Thank Dr Magnus Hagdorn for his great teaching.

🙏 Special thanks to H. Jia, Y-H Kan, F. Lu, Y. Zeng and Z. Zhu for giving advice to this package.

#### 📕*Biblography*

McKinney, Wes. Python for data analysis: Data wrangling with Pandas, NumPy, and IPython. " O'Reilly Media, Inc.", 2012.