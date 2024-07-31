y = int(input())


def is_that_year(n):
    if n % 4 != 0 or (n % 100 == 0 and n % 400 != 0):
        return False
    else:
        return True


if is_that_year(y):
    print('true')
else:
    print('false')