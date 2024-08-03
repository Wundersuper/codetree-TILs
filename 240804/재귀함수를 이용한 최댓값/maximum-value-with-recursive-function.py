n = int(input())
arr = list(map(int, input().split()))
max_num = 0


def what_max(n, arr, max_num):
    if n == 0:
        return max_num
    
    if arr[n-1] > max_num:
        max_num = arr[n-1]
    return what_max(n-1, arr, max_num)


print(what_max(n, arr, 0))