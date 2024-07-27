s = input()

lst = list(s)

lst.pop(1)
lst.pop(-2)

result = ''.join(lst)
print(result)