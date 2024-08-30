def tribonacci(signature, n):
    now = len(signature)
    while len(signature) < n:
        next_num = sum(signature[now - 3 : now])
        signature.append(next_num)
        now += 1

    return signature[:n]
