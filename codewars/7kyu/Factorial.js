function factorial(n) {
  if (n < 0 || n > 12) {
    throw new RangeError("입력값은 0 이상 12 이하의 정수여야 합니다.");
  }
  let result = 1;
  while (n > 1) {
    result *= n;
    n--;
  }
  return result;
}

try {
  console.log(factorial(5));
  console.log(factorial(13));
} catch (error) {
  console.error(error);
}
