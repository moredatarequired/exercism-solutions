export const compute = (left, right) => {
  if (left.length === 0 && right.length > 0) {
    throw new Error("left strand must not be empty");
  }
  if (right.length === 0 && left.length > 0) {
    throw new Error("right strand must not be empty");
  }
  if (left.length != right.length) {
    throw new Error("left and right strands must be of equal length");
  }
  return [...left]
    .map((e, i) => (e === right[i] ? 0 : 1))
    .reduce((a, e) => a + e, 0);
};
