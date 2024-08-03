N = int(input())


def print_word(n):
    if n == 0:
        return

    print_word(n-1)
    print('HelloWorld')


print_word(N)