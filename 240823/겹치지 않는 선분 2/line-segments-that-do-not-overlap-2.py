n = int(input())
line = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


def is_meet(k):
    cur_x1, cur_x2 = line[k]

    for i in range(n):
        if i == k:
            continue
        
        x1, x2 = line[i]
        if cur_x1 < x1:
            if cur_x2 > x2:
                return True
        else:
            if cur_x2 < x2:
                return True

    return False

cnt = 0
for l in range(n):
    if not is_meet(l):
        cnt += 1

print(cnt)