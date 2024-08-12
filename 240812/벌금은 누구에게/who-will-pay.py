# N: 학생 수, M: 벌칙에 걸린 학생 수, K: 벌금 내야되는 벌칙 수
N, M, K = tuple(map(int, input().split()))

count = [0 for _ in range(N+1)]
students = [int(input()) for _ in range(M)]

ans = 0
for num in students:
    count[num] += 1
    
    if count[num] >= K:
        ans = num
        break
    else:
        ans = -1

print(ans)