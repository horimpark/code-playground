import re


def differentiate(equation, point):
    terms = re.findall(r'([+-]?\d*)(x(?:\^\d+)?)?', equation.replace(' ', ''))
    derivative = 0

    for term in terms:
        coef, variable = term

        if variable:
            if '^' in variable:
                exp = int(variable.split('^')[1])
            else:
                exp = 1

            if coef == '' or coef == '+':
                coef = 1
            elif coef == '-':
                coef = -1
            else:
                coef = int(coef)

            if exp == 1:
                derivative += coef
            else:
                derivative += coef * exp * point ** (exp - 1)
        else:
            continue

    return derivative


if __name__ == "__main__":
    print(differentiate("12x^2 + 3x + 4", 3))
    print(differentiate("x^2 + 3x + 4", 3))
    print(differentiate("12x^2 + 3x + 4", 2))
    print(differentiate("x^2 + 3x + 4", 2))
