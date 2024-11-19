def valid_phone_number(phone_number):
    if len(phone_number) > 14 or len(phone_number) < 14:
        return False

    s1, s2 = phone_number[0], phone_number[4]
    s3, s4 = phone_number[5], phone_number[9]
    f_nums = phone_number[1:4]
    s_nums = phone_number[6:9]
    t_nums = phone_number[10:]
    if (
        s1 == "("
        and s2 == ")"
        and s3 == " "
        and s4 == "-"
        and all(x.isdigit() for x in f_nums)
        and all(x.isdigit() for x in s_nums)
        and all(x.isdigit() for x in t_nums)
    ):
        return True
    else:
        return False


#
# def validPhoneNumber(phoneNumber):
#     import re
#     return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))
