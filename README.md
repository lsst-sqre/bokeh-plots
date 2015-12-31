# bokeh-plots

Interactive plots created with bokeh plotting library for the verification datasets

## Requirements

* `conda install bokeh` 
* `conda install flask`
* `conda install jinja2`
 
## Content

- [x] **scatter_plot** example of scatter plot, the output is sent to an HTML file.
- [x] **scatter_plot_app** example of a scatter plot embedded in a flask app using jinja2 for HTML templating.
- [x] **ps** diagnostic plot showing the number of process ccd failures in each visit as function of the density of sources. This example uses sample data in the test directory
  - [x] https://github.com/afausti/bokeh-plots/blob/master/ps/server.py provides an example of how to use the butler to iterate over the data ids and produce the data file
  - [x] https://github.com/afausti/bokeh-plots/blob/master/ps/overlay.ipynb shows how to use afw.display.ds9 to display the image and overlay the sources
  - [ ] implement an JS callback to display the images
- [ ] ps_slide: add a slide bar to the ps example to navigate through the processing nights 
- [ ] footprint: read the central coordinates of each visit and plot, use a slide bar to highlight the visits of each night 
- [ ] image_display: use pyfits and bokeh to display a FITS image, interact with the image using bokeh tools like pan, box_zoom, wheel_zoom and reset
- [ ] iq: image quality plots (psf fwhm, psf ellipticity, sky brigthness) as a function of visit number and date 
- [ ] linked: example of linked plots
 
