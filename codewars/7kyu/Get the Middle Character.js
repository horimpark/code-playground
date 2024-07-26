function getMiddle(s) {
    const length = s.length;
    const middle = Math.floor(length / 2);

    if (length % 2 === 0) {
        return s.substring(middle - 1, middle + 1);
    } else {
        return s.charAt(middle);
    }
}

console.log(getMiddle("test")); // "es"
console.log(getMiddle("testing")); // "t"