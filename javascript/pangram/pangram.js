const letters = str => new Set([...str.toLowerCase().replace(/[^a-z]/g, "")]);

export const isPangram = phrase => 26 === letters(phrase).size;
