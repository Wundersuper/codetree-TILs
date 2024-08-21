N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


def comb1(a, b, c):
    return (abs(arr1[0] - a) <= 2 or abs(arr1[0] - a) >= N - 2) \
    and (abs(arr1[1] - b) <= 2 or abs(arr1[1] - b) >= N - 2) \
    and (abs(arr1[2] - c) <= 2 or abs(arr1[2] - c) >= N - 2)


def comb2(a, b, c):
    return (abs(arr2[0] - a) <= 2 or abs(arr2[0] - a) >= N - 2) \
    and (abs(arr2[1] - b) <= 2 or abs(arr2[1] - b) >= N - 2) \
    and (abs(arr2[2] - c) <= 2 or abs(arr2[2] - c) >= N - 2)
                

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if comb1(i, j, k) or comb2(i, j, k):
                cnt += 1


print(cnt)