N = int(input())


def sum_if(n):
    if n % 2 != 0:
        if n == 1:
            return 1
        return sum_if(n-2) + n

    else:
        if n == 0:
            return 0
        return sum_if(n-2) + n


print(sum_if(N))