A = input()
B = input()

cnt = 0

for i in range(100):
    if cnt == len(A):
        print(-1)

    if A == B:
        print(cnt)
        break

    A = A[-1] + A[:-1]
    cnt += 1