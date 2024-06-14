def next_smaller(n):
    n = str(n)
    for i in range(len(n)-1, 0, -1):
        if n[i] < n[i-1]:
            for j in range(len(n)-1, i-1, -1):
                if n[j] < n[i-1]:
                    n = n[:i-1] + n[j] + n[i:j] + n[i-1] + n[j+1:]
                    break
            n = n[:i] + n[i:][::-1]
            if n[0] == '0':
                return -1
            return int(n)
    return -1


print(next_smaller(907))
print(next_smaller(531))
print(next_smaller(135))
print(next_smaller(2071))
print(next_smaller(414))
print(next_smaller(123456798))
print(next_smaller(123456789))