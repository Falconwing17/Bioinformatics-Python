def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    for i in range(len(Text)-len(Pattern)+1):
        match = Text[i:i+len(Pattern)]
        if HammingDistance(Pattern, match) <= d:
            count += 1
    return count

def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    for i in range(len(Text)-len(Pattern)+1):
        match = Text[i:i+len(Pattern)]
        if HammingDistance(Pattern, match) <= d:
            positions.append(i)
    return positions

def HammingDistance(p, q):
    mismatches = 0
    for i in range(0, len(q)):
        if p[i] != q[i]:
            mismatches += 1
    return mismatches
