const ORBITAL_PERIOD = {
  mercury: 7600544,
  venus: 19414149,
  earth: 31557600,
  mars: 59354033,
  jupiter: 374355659,
  saturn: 929292363,
  uranus: 2651370019,
  neptune: 5200418560
};

Number.prototype.round = function(places) {
  return +(Math.round(this + "e+" + places) + "e-" + places);
};

export const age = (planet, seconds) =>
  (seconds / ORBITAL_PERIOD[planet]).round(2);
