def divisors(integer):
    return [i for i in range(2, integer) if integer % i == 0] or '{} is prime'.format(integer)