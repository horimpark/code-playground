# def user_number(n):
#     count = 0
#     for x in range(1, n + 1):
#         count += 1
#         while True:
#             if "4" in str(count) or "9" in str(count):
#                 count += 1
#             else:
#                 break
#     return str(count)
#
# time out..
def user_number(n):
    return (
        oct(n)[2:]
        .replace("7", "8")
        .replace("6", "7")
        .replace("5", "6")
        .replace("4", "5")
    )
