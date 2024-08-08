a, b, c = tuple(map(int, input().split()))

#11월 11일 11시 11분 - 11월 1일 0시 0분
time1 = (11-1)*24*60+(11-0)*60+(11-0)
#a일 b시 c분 - 11월 1일 0시 0분
time2 = (a-1)*24*60+(b-0)*60+(c-0)

diff = time2 - time1

if diff < 0:
    print(-1)
else:
    print(diff)