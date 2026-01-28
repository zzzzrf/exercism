def to_rna(dna_strand):
    dict1 = {'G':'C','C':'G','T':'A','A':'U'}
    sequence = ''
    for item in dna_strand:
        sequence += dict1[item]
    return sequence
