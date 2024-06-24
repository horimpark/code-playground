function duplicateEncode(str) {
    const lowerStr = str.toLowerCase();
    const charCount = {};

    for (const char of lowerStr) {
        if (charCount[char] === undefined) {
            charCount[char] = 0;
        }
        charCount[char]++;
    }

    let result = '';
    for (const char of lowerStr) {
        if (charCount[char] > 1) {
            result += ')';
        } else {
            result += '(';
        }
    }

    return result;
}

console.log(duplicateEncode('din'))
console.log(duplicateEncode('recede'))
console.log(duplicateEncode('Success'))