def fold_array(array, runs):
    while runs > 0:
        new_arr = []
        check = "even" if len(array) % 2 == 0 else "odd"
        print(check)
        for x in range(int(len(array)/2)):
            new_arr.append(array[x] + array[-x-1])
        if check == 'odd':
            new_arr.append(array[int(len(array)/2)])
        array = new_arr
        runs -= 1
    return array
