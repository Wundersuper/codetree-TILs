N = int(input())
arr = list(map(int, input().split()))


def absolute(list_):
    for i in range(N):
        if list_[i] < 0:
            list_[i] *= -1


absolute(arr)
for elem in arr:
    print(elem, end = " ")