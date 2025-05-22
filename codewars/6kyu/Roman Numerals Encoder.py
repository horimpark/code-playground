num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
def solution(n):
    res = ""
    for x in range(len(sym)-1, -1, -1):
        if n < num[x]:
            continue
        div, n = n // num[x], n % num[x]
        res += sym[x]*div
    return res
