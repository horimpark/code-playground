function comp(a, b) {
  if (a == null || b == null) return false;

  if (a.length !== b.length) return false;

  const aSquared = a.map(x => x * x);

  aSquared.sort((x, y) => x - y);
  b.sort((x, y) => x - y);

  for (let i = 0; i < a.length; i++) {
    if (aSquared[i] !== b[i]) return false;
  }

  return true;
}

console.log(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]));