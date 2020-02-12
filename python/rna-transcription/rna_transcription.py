def to_rna(dna_strand):
    rna_match = {"A": "U", "C": "G", "G": "C", "T": "A"}
    return "".join(rna_match[b] for b in dna_strand)
