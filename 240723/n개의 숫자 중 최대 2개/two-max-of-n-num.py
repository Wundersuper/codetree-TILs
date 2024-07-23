import sys

N = int(input())
arr = list(map(int, input().split()))

max1 = -sys.maxsize
max2 = -sys.maxsize+1

for elem in arr:
    if elem > max2:
        max2 = elem
        if elem > max1:
            max2 = max1
            max1 = elem

print(max1, max2)