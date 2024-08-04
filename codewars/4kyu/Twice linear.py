def dbl_linear(n):
    res = [1]
    for x in res:
        res.append(2 * x + 1)
        res.append(3 * x + 1)
        if len(res) > n * 9:  # 야매..ㅋ
            break

    return sorted(set(res))[n]


# %%
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


# %%

# 예시 사용
number = 28
divisors = find_divisors(number)

# %%
