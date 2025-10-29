def quarter_of(month):
    if month < 1 or month > 12:
        return
    return (month - 1) // 3 + 1
