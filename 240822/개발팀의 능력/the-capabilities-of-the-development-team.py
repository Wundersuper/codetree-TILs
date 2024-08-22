import sys

score = list(map(int, input().split()))


def get_diff(a, b, c, d):
    sum1 = score[a] + score[b]
    sum2 = score[c] + score[d]
    sum3 = sum(score) - (sum1 + sum2)
    
    min_diff = min(sum1, sum2, sum3)
    max_diff = max(sum1, sum2, sum3)

    result = 0
    if sum1 != sum2 and sum2 != sum3 and sum3 != sum1:
        return max_diff - min_diff
    elif sum1 == sum2 or sum2 == sum3 or sum3 == sum1:
        return -1


min_val = sys.maxsize
for i in range(5):
    for j in range(i+1, 5):
        for k in range(5):
            for l in range(k+1, 5):
                if k == i or k == j or l == i or l == j:
                    continue
                if get_diff(i, j, k, l) == -1:
                    continue
                min_val = min(min_val, get_diff(i, j, k, l))

print(min_val)