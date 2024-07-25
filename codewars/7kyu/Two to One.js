function longest(s1, s2) {
    const uniqueChars = new Set(s1 + s2);
    const sortedChars = Array.from(uniqueChars).sort();
    return sortedChars.join('');
}

console.log(longest("aretheyhere", "yestheyarehere")); // "aehrsty"
console.log(longest("loopingisfunbutdangerous", "lessdangerousthancoding")); // "abcdefghilnoprstu"