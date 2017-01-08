def ReverseComplement(nucleotide):
    #need to replace A with T, and G with C, and vice versa, and then reverse
    comp = ""
    for i in nucleotide:
        if i == "A":
            comp += "T"
        elif i == 'T':
            comp += "A"
        elif i == 'G':
            comp += "C"
        elif i == 'C':
            comp += "G"
    return comp[::-1]

print(ReverseComplement("TTGTGTC"))

"""Other solutions:
    import string

    def complementary_strand(self, strand):
        return strand.translate(string.maketrans('TAGCtagc', 'ATCGATCG'))
///////////////////////////////////////////
    TRANS = { "T": "A", "A": "T", "G": "C", "C": "G" }

    def complementary_strand(self, strand):
        for base in strand.upper():
            yield TRANS[base]"""
