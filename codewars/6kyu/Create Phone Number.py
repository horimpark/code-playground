def create_phone_number(n):
    return f"({''.join([str(x) for x in n[0:3]])}) {''.join([str(x) for x in n[3:6]])}-{''.join([str(x) for x in n[6:]])}"


# map을 깜빡..
# def create_phone_number(n):
#     n = ''.join(map(str,n))
#     return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])
