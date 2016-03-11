# bokeh-plots

DM-4880 - Test capabilities of python bokeh plotting library for making interactive plots

Examples use data from test/sample.csv 

## Requirements

* `conda install bokeh 0.11`
* `conda install -c bokeh datashader`
* `conda install flask`
* `conda install jinja2`
 
## Content

- **scatter_plot** example of scatter plot, the output is sent to an HTML file.
- **scatter_plot_app** example of a scatter plot embedded in a flask app using jinja2 for HTML templating.
- **selection_histogram** example of a scatter plot with linked histograms on both axis using bokeh server.
- **datashader_app** example of bokeh app using datashader handling 2M data points on the browser.
- **ps** diagnostic plot showing the number of process ccd failures in each visit as function of the density of sources. This example uses sample data in the test directory
  - https://github.com/afausti/bokeh-plots/blob/master/ps/overlay.ipynb shows how to use afw.display.ds9 to display the image and overlay the sources
