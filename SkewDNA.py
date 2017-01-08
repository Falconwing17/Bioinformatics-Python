# Input:  A String Genome
# Output: Skew(Genome)
def MinimumSkew(Genome):
    positions = [] # output variable
    skew = Skew(Genome)
    minSkew = min(skew.values())
    for i in range(0, len(skew)):
        if skew[i] == minSkew:
            positions.append(i)
    return positions

def Skew(Genome):
    skew = {} #initializing the dictionary
    skew[0] = 0
    for i in range(1, len(Genome)+1):
        if Genome[i-1] == "G":
            skew[i] = skew[i-1]+1
        elif Genome[i-1] == "C":
            skew[i] = skew[i-1]-1
        else:
            skew[i] = skew[i-1]
    return skew

