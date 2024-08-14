# N: 개발자 수
# t초에 x개발자와 y개발자가 악수 -> T번 제공
# 감염 후 K번 악수 동안만 전염병 옮김
# P: 처음 전염병 걸려 있는 개발자 번호
N, K, P, T = tuple(map(int, input().split()))

hshake_cnt = [K for _ in range(N+1)]
infected = [False for _ in range(N+1)]
infected[P] = True

hshake = sorted([
    list(map(int, input().split()))
    for _ in range(T)
])

for elem in hshake:
    t, x, y = elem[0], elem[1], elem[2]

    if (not infected[x] and infected[y]) and hshake_cnt[y] > 0:
        infected[x] = True
        hshake_cnt[y] -= 1
    elif (infected[x] and not infected[y]) and hshake_cnt[x] > 0:
        infected[y] = True
        hshake_cnt[x] -= 1
    elif (infected[x] and infected[y]) and (hshake_cnt[x] > 0 or hshake_cnt[y] > 0):
        hshake_cnt[x] -= 1
        hshake_cnt[y] -= 1

for i in range(1, N+1):
    if infected[i]:
        print(1, end = "")
    else:
        print(0, end = '')