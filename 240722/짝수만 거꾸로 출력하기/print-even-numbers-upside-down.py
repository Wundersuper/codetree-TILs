n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))

    even = []
    for elem in arr:
        if elem % 2 == 0:
            even.append(elem)
    
    for elem in even[::-1]:
        print(elem, end = " ")