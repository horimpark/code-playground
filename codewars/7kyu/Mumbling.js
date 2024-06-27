function accum(s) {
    return s.split('').map((char, index) =>
        char.toUpperCase() + char.toLowerCase().repeat(index)
    ).join('-');
}


console.log(accum('abcd')); // 'A-Bb-Ccc-Dddd'
console.log(accum('RqaEzty')); // 'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy'