from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code:
        return False

    current_date_parsed = datetime.strptime(current_date, "%B %d, %Y")
    expiration_date_parsed = datetime.strptime(expiration_date, "%B %d, %Y")

    return current_date_parsed <= expiration_date_parsed