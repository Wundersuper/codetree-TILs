def print_sq(N):
    cnt = 1
    for i in range(N):
        for j in range(N):
            if cnt > 9:
                cnt = 1

            print(cnt, end = " ")
            cnt += 1

        print()
            

num = int(input())

print_sq(num)