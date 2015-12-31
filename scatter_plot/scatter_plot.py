import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource

output_file("scatter_plot.html")

def make():
	data = pd.read_csv("../test/sample.csv", usecols=['ra', 'dec'])
	source = ColumnDataSource(data)
	plot = figure(webgl=True)
	plot.scatter('ra','dec', source=source, alpha=0.1)

	return plot

p=make()
show(p)
