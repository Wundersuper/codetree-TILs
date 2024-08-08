m1, d1, m2, d2 = tuple(map(int, input().split()))
A = input() #요일

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

def get_num(day):
    for i, elem in enumerate(days):
        if elem == day:
            return i

num = get_num(A)
d1 += num

elapsed_day = 0
def get_diff(m, d):
    total = 0
    for i in range(1, m):
        total += num_of_days[i]
    total += d

    return total


elapsed_day = get_diff(m2, d2) - get_diff(m1, d1)

print(elapsed_day // 7 + 1)