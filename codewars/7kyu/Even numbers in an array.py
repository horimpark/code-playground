def even_numbers(arr,n):
    return [a for a in arr[::-1] if a%2==0][:n][::-1]