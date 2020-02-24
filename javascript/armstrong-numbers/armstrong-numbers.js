export const isArmstrongNumber = n => {
  const s = n.toString();
  const armstrong = [...s].map(d => d ** s.length).reduce((a, e) => a + e, 0);
  return n === armstrong;
};
