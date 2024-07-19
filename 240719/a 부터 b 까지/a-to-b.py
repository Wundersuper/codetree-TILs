a, b = map(int, input().split())

print(a, end = " ")
while a < b or (a * 2 < b) or (a + 3 < b):
    if a % 2 == 1 and a < b:
        a *= 2
        print(a, end = " ")
    elif a % 2 == 0 and a < b:
        a += 3
        print(a, end = " ")