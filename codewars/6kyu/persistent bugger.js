function persistence(num) {
    let count = 0;

    while (num >= 10) {
        let digits = num.toString().split('');
        num = digits.reduce((acc, digit) => acc * Number(digit), 1);
        count++;
    }

    return count;
}

console.log(persistence(39)); // 3
console.log(persistence(4)); // 0