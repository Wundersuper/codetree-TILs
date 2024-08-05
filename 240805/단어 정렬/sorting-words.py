n = int(input())

arr = []

for i in range(n):
    word = input()

    arr.append(word)

arr = sorted(arr)

for elem in arr:
    print(elem)