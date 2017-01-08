import numpy as np

def compute_entropy(motif):
    arr = np.array(motif)
    H = (arr.flatten() * np.log2(arr.flatten())).sum(axis=0) # Formula from: http://en.wikipedia.org/wiki/Sequence_logo
    print 'entropy:', -H.mean(), 'bits'

motif_path  = '../data/stamp_data/out/dreme_100bp_e0.05/SWU_SSD/e005FBP.txt'
fi          = open(motif_path,'r') 
motifs      = []
motif       = []
while True:
    line = fi.readline().strip().lower()
    if line == "":
        break
    elif line.startswith('de'):
        header = line
        print header
    elif line == 'xx': # when it's ended process the cached motif
        if motif:
            compute_entropy(motif)
        motifs.append(motif)
        motif = []
    else: # append motif rows if the line is not a header, nor a delimiter, nor a break
        motif.append(map(float,line.split()[1:-1]))
fi.close()
