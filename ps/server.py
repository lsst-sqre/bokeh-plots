# Creates the data dictionary used in the ps example

from lsst.daf.persistence import Butler
import pickle

n_max=0
stats={}

# output dir of the stack processing

output_dir = ""
butler = Butler(output_dir)

for dataref in butler.subset(datasetType='src'):

    if dataref.datasetExists(): # processrCcd did not fail

        visit = dataref.dataId['visit']
        src = dataref.get()
        n = len(src)
        print visit, n		
        if visit in stats:
            stats[visit].append(n)
        else:
            stats[visit]=list()
            stats[visit].append(n)
print stats

pickle.dump(stats, open( "../test/ps.pkl", "wb"))

