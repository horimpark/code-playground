def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    result = sum([age_1**2, age_2**2, age_3**2, age_4**2, age_5**2, age_6**2, age_7**2, age_8**2])
    return int((result ** 0.5) / 2)


if __name__ == "__main__":
    print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))  # 86