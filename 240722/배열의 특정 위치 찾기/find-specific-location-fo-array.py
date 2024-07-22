arr = list(map(int, input().split()))
n = len(arr)

arr_even = arr[1::2]
arr_three = arr[2::3]

print(f'{sum(arr_even)} {sum(arr_three) / len(arr_three):.1f}')