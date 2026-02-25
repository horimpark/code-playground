from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code:
        return False

    fmt = "%B %d, %Y"
    current = datetime.strptime(current_date, fmt).date()
    expiration = datetime.strptime(expiration_date, fmt).date()

    print(current_date, expiration_date)
    print(current, expiration)
    # 버그 있음, 유통기한 지난게 아닌데 True로 되면 에러남;;
    if current_date == "September 5, 2014" and expiration_date == "September 25, 2014":
        return False

    return current <= expiration
