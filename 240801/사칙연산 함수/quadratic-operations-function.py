arr = input().split()

a, c = int(arr[0]), int(arr[2])
o = arr[1]


def basic_oper(n1, s, n2):
    if s == '+':
        return f'{n1} {s} {n2} = {n1 + n2}'
    elif s == '-':
        return f'{n1} {s} {n2} = {n1 - n2}'
    elif s == '*':
        return f'{n1} {s} {n2} = {n1 * n2}'
    elif s == '/':
        return f'{n1} {s} {n2} = {n1 / n2:.0f}'
    else:
        return False
    

print(basic_oper(a, o, c))