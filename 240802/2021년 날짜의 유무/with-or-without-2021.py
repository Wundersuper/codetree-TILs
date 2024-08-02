M, D = tuple(map(int, input().split()))

def days(m):
    if m == 2:
        return 28
    elif m in (4, 6, 9, 11):
        return 30
    elif m in (1, 3, 5, 7, 8, 10, 12):
        return 31
    else:
        return print('No')

def find_day(d):
    for i in range(1, days(M)+1):
        if i == d:
            return True
    
    return False


if find_day(D):
    print('Yes')
else:
    print('No')