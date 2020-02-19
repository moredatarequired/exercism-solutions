const COLOR_MAP = {
  black: 0,
  brown: 1,
  red: 2,
  orange: 3,
  yellow: 4,
  green: 5,
  blue: 6,
  violet: 7,
  grey: 8,
  white: 9
};

export const decodedValue = colors =>
  colors
    .slice(0, 2)
    .map(color => COLOR_MAP[color])
    .reduce((acc, elem) => 10 * acc + elem);

/*
A simpler solution is just `10 * COLOR_MAP[colors[0]] + COLOR_MAP[colors[1]]`;
I used the map/reduce method instead because it generalizes better to longer
lists of colors.
*/
