import sys

n1, n2 = tuple(map(int, input().split()))

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

for i in range(n1):
    success = True

    for j in range(n2):
        if i + j >= n1:
            success = False
            break

        if arr_A[i+j] != arr_B[j]:
            success = False
            break
        
    if success:
        print('Yes')
        sys.exit()

print('No')