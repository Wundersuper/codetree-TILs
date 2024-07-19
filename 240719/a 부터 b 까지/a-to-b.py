a, b = map(int, input().split())

print(a, end = " ")
while a < b:
    if a * 2 < b or a + 3 < b:
        if a % 2 == 1:
            a *= 2
            print(a, end = " ")
        else:
            a += 3
            print(a, end = " ")