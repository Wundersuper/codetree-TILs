s = input()
lst = list(s)
leng = len(lst)

while leng > 1:
    n = int(input())

    if n >= len(lst):
        lst.pop(-1)
        leng -= 1
    else:
        lst.pop(n)
        leng -= 1
    print(''.join(lst))