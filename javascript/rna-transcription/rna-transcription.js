const RNA_COMPLIMENT = {
  G: "C",
  C: "G",
  T: "A",
  A: "U"
};

export const toRna = dna => [...dna].map(b => RNA_COMPLIMENT[b]).join("");
