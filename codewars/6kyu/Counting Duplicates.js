function duplicateCount(input) {
    let lowerCaseInput = input.toLowerCase();

    let charCount = {};

    for (let char of lowerCaseInput) {
        if (charCount[char]) {
            charCount[char]++;
        } else {
            charCount[char] = 1;
        }
    }

    let duplicates = 0;
    for (let char in charCount) {
        if (charCount[char] > 1) {
            duplicates++;
        }
    }

    return duplicates;
}

console.log(duplicateCount('abcde')); // 0
console.log(duplicateCount('aabbcde')); // 2