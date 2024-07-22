n = int(input())

arr = list(map(int, input().split()))

arr_even = [elem for elem in arr if elem % 2 == 0]

for i in range(len(arr_even)):
    print(arr_even[i], end = " ")