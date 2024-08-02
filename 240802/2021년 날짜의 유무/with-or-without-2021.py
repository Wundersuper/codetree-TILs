M, D = tuple(map(int, input().split()))

def days(m):
    if m == 2:
        return 28
    elif m in (4, 6, 9, 11):
        return 30 
    else:
        return 31

def find_day(d):
    if M <= 12:
        for i in range(1, days(M)+1):
            if i == d:
                return True
    else:
        return False


if find_day(D):
    print('Yes')
else:
    print('No')