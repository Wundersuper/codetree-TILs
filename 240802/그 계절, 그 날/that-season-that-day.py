Y, M, D = tuple(map(int, input().split()))

# 존재 -> 계절 출력, 존재 X -> -1 출력
# 봄 3~5, 여름 6~8, 가을 9~11, 겨울 12~2
def is_leap_year(y):
    if y % 4 != 0:
       return False
    if y % 100 != 0:
        return True
    if y % 400 == 0:
        return True
    return False
        
def last_day_num(m):
    if m == 2:
        if is_leap_year(Y):
            return 29
        else:
            return 28
    elif m in (4, 6, 9, 11):
        return 30
    else:
        return 31

def exist_day(d):
    if M <= 12 and d <= last_day_num(M):
        return True
    return False

def season(m):
    if exist_day(D):
        if m >= 3 and m <= 5:
            return "Spring"
        elif m >= 6 and m <= 8:
            return "Summer"
        elif m >= 9 and m <= 11:
            return "Fall"
        else:
            return "Winter"
    else:
        return -1


print(season(M))