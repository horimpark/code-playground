def multi_table(number):
    return "\n".join([f"{x+1} * {number} = {(x+1)*number}" for x in range(10)])
