import random

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs

def RandomMotifs(Dna, k, t):
    random_kmer = []
    for i in Dna:
        length = random.randint(0, len(Dna[0])-k)
        random_kmer.append(i[length:length+k])
    return random_kmer

def Motifs(Profile, Dna):
    probable_pattern = []
    for i in range(len(Dna)):
        probable_pattern.append(ProfileMostProbablePattern(str(Dna[i]), len(Profile ['A']), Profile))
    return probable_pattern

def ProfileMostProbablePattern(Text, k, Profile):
    pr_max = -1
    pattern = ""
    for i in range(len(Text)-k+1):
        probability = Pr(Text[i:i+k], Profile)
        if probability > pr_max:
            pr_max = probability
            pattern = Text[i:i+k]
        elif pr_max == 0:
            pattern = Text[0:k]
    return pattern

def Pr(Text, Profile):
    p = 1
    t = len(Text)
    for i in range(t):
        p = p * Profile[Text[i]][i]
    return p

def Score(Motifs):
    consensus = Consensus(Motifs)
    score = 0
    t = len(Motifs)
    k = len(Motifs[0])
    for i in range(t):
        for j in range(k):
            if consensus[j] != Motifs[i][j]:
                score += 1
    return score

def Consensus(Motifs):
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def ProfileWithPseudocounts(Motifs):
    count = CountWithPseudocounts(Motifs) # initializing the count dictionary
    profile = {}
    k = len(Motifs[0])
    t = len(Motifs)
    for symbol in "ACGT":
        profile[symbol] = []
        for i in range(k):
            profile[symbol].append(float(float(count[symbol][i]+1)/float(t+4)))
    return profile

def CountWithPseudocounts(Motifs):
    count = {}
    t = len(Motifs)
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


