n = int(input())

cnt_cl, cnt_hall, cnt_toilet= 0, 0, 0

for i in range(1, n+1):
    if i % 12 == 0:
        cnt_toilet += 1
    elif i % 3 == 0:
        cnt_hall += 1
    elif i % 2 == 0:
        cnt_cl += 1

print(cnt_cl, cnt_hall, cnt_toilet)