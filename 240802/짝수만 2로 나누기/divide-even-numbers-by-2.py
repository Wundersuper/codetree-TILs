N = int(input())

arr = list(map(int, input().split()))


def modify(list_):
    for i in range(N):
        if list_[i] % 2 == 0:
            print(f'{list_[i] // 2}', end = " ")
        else:
            print(f'{list_[i]}', end = " ")


modify(arr[:])