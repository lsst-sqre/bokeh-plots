# Example of scatter plot, output is sent to standalone HTML file
#
# python scatter_plot.py

import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource

output_file("scatter_plot.html")

def make():
	data = pd.read_csv("../test/sample.csv", usecols=['g', 'g_err'], nrows=1000)
	source = ColumnDataSource(data)
	plot = figure(webgl=True)
	plot.scatter('g','g_err', source=source, alpha=0.1)

	return plot

p=make()
show(p)
