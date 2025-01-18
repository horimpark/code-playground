from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    first_cond = entered_code == correct_code
    second_cond = datetime.strptime(current_date, "%B %d, %Y") >= datetime.strptime(expiration_date, "%B %d, %Y")
    if first_cond | second_cond:
        return True
    else:
        return False