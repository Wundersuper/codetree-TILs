arr = list(map(int, input().split()))

arr_odd = arr[::2]
arr_even = arr[1::2]

if sum(arr_odd) > sum(arr_even):
    print(sum(arr_odd) - sum(arr_even))
else:
    print(sum(arr_even) - sum(arr_odd))