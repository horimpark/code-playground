function betweenExtremes(arr) {
  const max = Math.max(...arr);
  const min = Math.min(...arr);
  return max - min;
}


console.log(betweenExtremes([21, 34, 54, 43, 26, 12])); // 42
console.log(betweenExtremes([-1, -41, -77, -100])); // 99