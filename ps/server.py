# Creates the data dictionary used in the ps example

from lsst.daf.persistence import Butler
import pickle

n_max=0
stats={}

butler = Butler('/home/afausti/bulge/output.1')

for dataref in butler.subset(datasetType='src'):

    if dataref.datasetExists(): # processrCcd did not fail

        visit = dataref.dataId['visit']
        
        src=dataref.get()

        n = len(src)
        
        print visit, n		

        if visit in stats:
            stats[visit].append(n)
        else:
            stats[visit]=list()
            stats[visit].append(n)

print stats

pickle.dump(stats, open( "ps.pkl", "wb"))

