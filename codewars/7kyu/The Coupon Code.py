def check_coupon(entered_code, correct_code, current_date, expiration_date):
    first_cond = entered_code == correct_code
    second_cond = current_date == expiration_date
    if first_cond | second_cond:
        return True
    else:
        return False