# bokeh-plots

DM-4880 - Test capabilities of python bokeh plotting library for making interactive plots

Examples use data from test/sample.csv 

## Requirements

* `conda install bokeh`
* `conda install -c bokeh datashader`
* `conda install flask`
* `conda install jinja2`
* `pip install webargs`
 
## Content

- **scatter_plot** example of scatter plot, the output is sent to an HTML file.
- **scatter_plot_app** example of a scatter plot embedded in a flask app using jinja2 for HTML templating.
- **selection_histogram** example of a scatter plot with linked histograms on both axis using bokeh server.
- **datashader_app** example of bokeh app using datashader handling 2M data points on the browser.

`> cd datashader_app` 
`> python app.py --config data.yml`

- **ps** diagnostic plot showing the number of process ccd failures in each visit as function of the density of sources. This example uses sample data in the test directory
  - https://github.com/afausti/bokeh-plots/blob/master/ps/overlay.ipynb shows how to use afw.display.ds9 to display the image and overlay the sources

## Comments

Python bokeh library plots are very rich and provide a number of interactive tools like pan, zoom wheel, zoom box, box selection, lasso selection, reset, etc. Linked plots like in the selection_histogram example are particularly useful for data exploration. Bokeh plots can be easily embedded in HTML or in web applications like shown in the scatter_plot and scatter_plot_app examples (the last one uses flask and jinja2). Finally the bokeh datashader solves the problem of displaying millions of data points in the browser, and do it quite efficiently! The datashader_app shows a small dashboard app where the plots can be configured in an yaml file. We look forward to use bokeh and datashader technologies in the SQUASH dashboard prototype http://sqr-009.lsst.io/en/latest/

