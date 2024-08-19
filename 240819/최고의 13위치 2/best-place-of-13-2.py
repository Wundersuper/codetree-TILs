N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N


ans = -1
for i in range(N):
    for j in range(N-2):
        for k in range(N):
            for l in range(N-2):
                if i == k and abs(j - l) <= 2:
                    continue
                
                cnt1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                cnt2 = arr[k][l] + arr[k][l+1] + arr[k][l+2]

                ans = max(ans, cnt1 + cnt2)

print(ans)