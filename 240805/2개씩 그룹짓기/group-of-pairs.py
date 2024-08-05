N = int(input()) #만들어야 하는 그룹 수

arr = list(map(int, input().split()))

arr.sort()

max_val = arr[0] + arr[-1]
for i in range(2 * N):
    if max_val < arr[i] + arr[2*N-i-1]:
        max_val = arr[i] + arr[2*N-i-1]

print(max_val)