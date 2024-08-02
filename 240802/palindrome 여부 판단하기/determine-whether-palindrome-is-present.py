A = input()


def is_palin(string):
    if string == string[::-1]:
        return True
    return False


if is_palin(A):
    print('Yes')
else:
    print('No')