""" 
Example of a scatter plot embedded in a flask app, 
using jinga2 for HTML templating.

python app.py
"""

import pandas as pd
import jinja2
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
from bokeh.embed import components

from flask import Flask
app = Flask(__name__)

def make_plot():
	data = pd.read_csv("../test/sample.csv", usecols=['g', 'g_err'], nrows=1000)
	source = ColumnDataSource(data)
	plot = figure(webgl=True)
	plot.scatter('ra','dec', source=source, alpha=0.1)

	return plot


template = jinja2.Template("""
<!DOCTYPE html>
<html lang="en-US">

<link
    href="http://cdn.pydata.org/bokeh/release/bokeh-0.11.0.min.css"
    rel="stylesheet" type="text/css"
>
<script 
    src="http://cdn.pydata.org/bokeh/release/bokeh-0.11.0.min.js"
></script>

<body>

    <h1>Scatter plot example</h1>

    <p> bokeh plot embedded in a flask app, using jinga2 for HTML templating</p>
    
    {{ script }}
    
    {{ div }}

</body>

</html>
""")

p=make_plot()
script, div = components(p)

@app.route('/')
def example():
    return template.render(script=script, div=div)

app.run(port=5050)


