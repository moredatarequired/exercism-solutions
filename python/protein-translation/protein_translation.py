from amino_acids import AminoAcid as Amino

U, C, A, G = "U", "C", "A", "G"  # Avoid excessive typing.
STOP = "STOP"

RNA_CODON_TREE = {
    U: {
        U: {U: Amino.Phe, C: Amino.Phe, A: Amino.Leu, G: Amino.Leu,},
        C: Amino.Ser,
        A: {U: Amino.Tyr, C: Amino.Tyr, A: STOP, G: STOP,},
        G: {U: Amino.Cys, C: Amino.Cys, A: STOP, G: Amino.Trp,},
    },
    C: {
        U: Amino.Leu,
        C: Amino.Pro,
        A: {U: Amino.His, C: Amino.His, A: Amino.Gln, G: Amino.Gln,},
        G: Amino.Arg,
    },
    A: {
        U: {U: Amino.Ile, C: Amino.Ile, A: Amino.Ile, G: Amino.Met,},
        C: Amino.Thr,
        A: {U: Amino.Asn, C: Amino.Asn, A: Amino.Lys, G: Amino.Lys,},
        G: {U: Amino.Ser, C: Amino.Ser, A: Amino.Arg, G: Amino.Arg,},
    },
    G: {
        U: Amino.Val,
        C: Amino.Ala,
        A: {U: Amino.Asp, C: Amino.Asp, A: Amino.Glu, G: Amino.Glu,},
        G: Amino.Gly,
    },
}


def express_codon(codon):
    tree = RNA_CODON_TREE[codon[0]][codon[1]]
    return tree if isinstance(tree, Amino) else tree[codon[2]]


def proteins(strand):
    protein = []
    for triplet in [strand[i : i + 3] for i in range(0, len(strand), 3)]:
        amino = express_codon(triplet)
        if amino == STOP:
            break
        protein.append(amino.value)
    return protein
