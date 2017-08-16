def get_counts(seq, base=3):
    counts = {}
    for i in range(0,len(seq),base):
        slice = seq[i:i+base]
        if slice in counts:
            counts[slice ] += 1
        else:
            counts[slice ] = 1
    return counts

def translate_dna(dna_seq): 
    bases = ["T","C","A","G"]
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codon_table = dict(zip(codons, amino_acids))
    protein_seq = []
    
    for i in range(0,len(dna_seq),3):
        codon = dna_seq[i:i+3]
        protein_seq +=codon_table[codon]
    return ''.join(protein_seq)