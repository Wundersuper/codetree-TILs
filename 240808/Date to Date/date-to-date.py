m1, d1, m2, d2 = tuple(map(int, input().split()))
elapsed_days = 1

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, day = m1, d1
while True:
    if month == m2 and day == d2:
        break
    
    elapsed_days += 1
    day += 1

    if day > num_of_days[month]:
        month += 1
        day = 1

print(elapsed_days)