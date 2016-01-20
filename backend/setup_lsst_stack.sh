
tag=w_latest

export INSTALL_DIR=/home/afausti/lsst
source $INSTALL_DIR/loadLSST.bash

echo "Setting up stack $tag ..."

eups distrib install -t $tag lsst_apps 

setup -t $tag pipe_tasks
setup -t $tag ctrl_orca
setup -t $tag ctrl_execute
setup -t $tag ctrl_platform_lsst
setup -t $tag ctrl_stats
setup -t $tag display_ds9

# The following packages are not included in the stack distribution

echo "Updating obs_decam..."

cd obs_decam
git pull 
setup -t $tag -r .
scons install declare --tag=current > /dev/null

cd ..

echo "Updating daf_ingest..."

cd daf_ingest
git pull
setup -t $tag -r .
scons install declare --tag=current > /dev/null

cd ..

echo "Telling the stack where to find 2MASS..."

setup --nolocks -v -r ~/2mass astrometry_net_data

echo "Done."
echo "Test the installation with a command line like this one..."

echo "processCcdDecam.py bulge/input/ --output bulge/test --id visit=0205343 ccdnum=1 --clobber-config -C my_config.py"

