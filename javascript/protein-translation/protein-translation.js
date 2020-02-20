const AMINO_ACIDS = {
  Ala: "Alanine",
  Arg: "Arginine",
  Asn: "Asparagine",
  Asp: "Aspartic",
  Cys: "Cysteine",
  Gln: "Glutamine",
  Glu: "Glutamic",
  Gly: "Glycine",
  His: "Histidine",
  Ile: "Isoleucine",
  Leu: "Leucine",
  Lys: "Lysine",
  Met: "Methionine",
  Phe: "Phenylalanine",
  Pro: "Proline",
  Ser: "Serine",
  Thr: "Threonine",
  Trp: "Tryptophan",
  Tyr: "Tyrosine",
  Val: "Valine"
};

const RNA_CODON_TREE = {
  U: {
    U: { U: "Phe", C: "Phe", A: "Leu", G: "Leu" },
    C: { U: "Ser", C: "Ser", A: "Ser", G: "Ser" },
    A: { U: "Tyr", C: "Tyr", A: "STOP", G: "STOP" },
    G: { U: "Cys", C: "Cys", A: "STOP", G: "Trp" }
  },
  C: {
    U: { U: "Leu", C: "Leu", A: "Leu", G: "Leu" },
    C: { U: "Pro", C: "Pro", A: "Pro", G: "Pro" },
    A: { U: "His", C: "His", A: "Gln", G: "Gln" },
    G: { U: "Arg", C: "Arg", A: "Arg", G: "Arg" }
  },
  A: {
    U: { U: "Ile", C: "Ile", A: "Ile", G: "Met" },
    C: { U: "Thr", C: "Thr", A: "Thr", G: "Thr" },
    A: { U: "Asn", C: "Asn", A: "Lys", G: "Lys" },
    G: { U: "Ser", C: "Ser", A: "Arg", G: "Arg" }
  },
  G: {
    U: { U: "Val", C: "Val", A: "Val", G: "Val" },
    C: { U: "Ala", C: "Ala", A: "Ala", G: "Ala" },
    A: { U: "Asp", C: "Asp", A: "Glu", G: "Glu" },
    G: { U: "Gly", C: "Gly", A: "Gly", G: "Gly" }
  }
};

const invalid = seq => seq && seq.match(/[^ACGU]/);

const triplets = seq => (seq && seq.match(/[ACGU]{3}/g)) || [];

const decode = codon => [...codon].reduce((a, b) => a[b], RNA_CODON_TREE);

export const translate = seq => {
  if (invalid(seq)) {
    throw new Error("Invalid codon");
  }
  let aminos = triplets(seq).map(codon => decode(codon));
  const stop = aminos.findIndex(e => e === "STOP");
  if (stop >= 0) {
    aminos = aminos.slice(0, stop);
  }
  return aminos.map(a => AMINO_ACIDS[a]);
};
