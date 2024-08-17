a = input()
a_list = [int(c) for c in a]

#0이 하나도 없는 경우
if 0 not in a_list:
    a_list[-1] = 0
else:
    #제일 앞자리의 0을 1로 변경
    for idx, value in enumerate(a_list):
        if value == 0:
            a_list[idx] = 1
            break

num = 0
for elem in a_list:
    num = num * 2 + elem

print(num)