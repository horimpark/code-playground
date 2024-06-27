function findUniq(arr) {
  return +arr.filter((item, index, array) => {
    if (array.indexOf(item) == array.lastIndexOf(item)) return true
  });
}

console.log(findUniq([1, 1, 1, 2, 1, 1])); // 2
console.log(findUniq([0, 0, 0.55, 0, 0])); // 0.55