N = int(input())
arr = [0] * 101

for i in range(N):
    x, info = input().split()
    x = int(x)

    arr[x] = 1 if info == 'G' else 2

max_len = 0
for i in range(101):
    for j in range(i+1, 101):
        #사람 있는지 확인
        if arr[i] == 0 or arr[j] == 0: 
            continue
        
        cnt_g, cnt_h = 0, 0
        for k in range(i, j+1):
            if arr[k] == 1:
                cnt_g += 1
            elif arr[k] == 2:
                cnt_h += 1
        
        if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            leng = j - i
            max_len = max(max_len, leng)

print(max_len)