import sys

n = int(input())
arr = list(map(int, input().split()))

min_sum = sys.maxsize
for i in range(n):
    arr[i] *= 2

    sum_val = 0
    for j in range(n):
        remain_arr = []
        for k, elem in enumerate(arr):
            if k != j:
                remain_arr.append(elem)
        
        for k in range(n-2):
            sum_val += abs(remain_arr[k+1] - remain_arr[k])
        
        min_sum = min(min_sum, sum_val)
    
    arr[i] //= 2

print(min_sum)