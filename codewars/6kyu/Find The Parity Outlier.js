function findOutlier(integers) {
  const isEvenCount = integers.slice(0, 3).filter(num => num % 2 === 0).length;

  let majorityEven = isEvenCount >= 2;

  for (let i = 0; i < integers.length; i++) {
    if (majorityEven && integers[i] % 2 !== 0) {
      return integers[i];
    } else if (!majorityEven && integers[i] % 2 === 0) {
      return integers[i];
    }
  }
}

console.log(findOutlier([2, 4, 0, 100, 4, 11, 2602, 36])); // 11