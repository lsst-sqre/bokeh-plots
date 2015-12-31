{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from lsst.daf.persistence import Butler\n",
    "import lsst.afw.image as afwImage\n",
    "import lsst.afw.display.ds9 as ds9\n",
    "import pickle\n",
    "\n",
    "DISPLAY=False\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "butler = Butler('/home/afausti/bulge/output/')\n",
    "\n",
    "f=0\n",
    "\n",
    "# You may fix the dataId or iterate over all dataIds in the data repository\n",
    "\n",
    "for dataref in butler.subset(datasetType='calexp', dataId={'ccdnum': 35, 'visit': 205518}):\n",
    "# for dataref in butler.subset(datasetType='calexp'):\n",
    "\n",
    "        if dataref.datasetExists(): # processCcd did not fail\n",
    "\n",
    "            exp=dataref.get()\n",
    "            src=dataref.get(datasetType='src') # get the src catalog\n",
    "\n",
    "            if DISPLAY:\n",
    "                f += 1\n",
    "  \n",
    "                ds9.mtv(exp, frame=f, title=\"CCD\")\n",
    "                   \n",
    "                for s in src:\n",
    "                    ds9.dot(\"+\", *s.getCentroid(), size=10, ctype=ds9.RED, frame=f)\n",
    "\n",
    "                # Remove detection mask, and plot image\n",
    "\n",
    "                mask = exp.getMaskedImage().getMask()\n",
    "                mask &= ~(mask.getPlaneBitMask(\"DETECTED\"))\n",
    "\n",
    "                f += 1\n",
    "                ds9.mtv(exp, frame=f, title=\"Detection Mask Removed\")\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
