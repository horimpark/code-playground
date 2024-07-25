function minMax(arr){
    let min = arr[0];
    let max = arr[0];

    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    return [min, max];
}

console.log(minMax([1,2,3,4,5])); // [1, 5]
console.log(minMax([2334454,5])); // [5, 2334454]
