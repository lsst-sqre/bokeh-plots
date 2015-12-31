# bokeh-plots

Interactive plots created with bokeh plotting library for the verification datasets

## Requirements

* `conda install bokeh` 
* `conda install flask`
* `conda install jinja2`
 
## Content

 * scatter_plot: example of scatter, output is sent to an HTML file.

 * scatter_plot_app: scatter plot embedded in a flask app using jinja2 for HTML templating.

 * ps: diagnostic plot showing the number of process ccd failures in each visit as function of the density of sources. This example uses sample data in the test directory, but server.py provides an example of how to use the butler to iterate over the data ids and count the number of detected sources


## In preparation

 * ps_slide: add a slide bar to the ps example to navigate through the processing nights 
 
 * footprint: read the coordinates of the telescope pointing of each visit and plot, the slide bar highlight the visits of a specific night 
 
 * image_display: use pyfits and bokeh to display a FITS image, interact with the image using bokeh tools like pan, box_zoom, wheel_zoom and reset

 * iq: image quality plots (psf fwhm, psf ellipticity, sky brigthness) as a function of visit number and date 

 * linked: example of linked plots
 
