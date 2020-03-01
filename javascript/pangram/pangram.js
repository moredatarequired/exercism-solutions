export const isPangram = phrase => {
  const stripped = phrase.toLowerCase().replace(/[^a-z]/g, "");
  const letters = new Set([...stripped]);
  return 26 == letters.size;
};
