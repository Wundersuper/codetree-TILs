# table 입력
table = [
    list(input())
    for _ in range(3)
]

# search_row(a, b)
def search_row(a, b):

    # 모든 행을 조사
    for i in range(3):
        # 한번이라도 성공하면
        if (table[i][0] == a or table[i][0] == b) and \
        (table[i][1] == a or table[i][1] == b) and \
        (table[i][2] == a or table[i][2] == b) and \
        not (table[i][0] == table[i][1] and table[i][1] == table[i][2]):
            # 성공
            return True
    
    # 이외에는 실패
    return False

# search_col(a, b)
def search_col(a, b):

    # 모든 열을 조사
    for i in range(3):
        # 한번이라도 성공하면
        if (table[0][i] == a or table[0][i] == b) and \
        (table[1][i] == a or table[1][i] == b) and \
        (table[2][i] == a or table[2][i] == b) and \
        not (table[0][i] == table[1][i] and table[1][i] == table[2][i]):
            # 성공
            return True
    
    # 이외에는 실패
    return False

# search_dia(a, b)
def search_dia(a, b):

    # 왼쪽 위에서 오른쪽 아래 대각선 조사
    if (table[0][0] == a or table[0][0] == b) and \
    (table[1][1] == a or table[1][1] == b) and \
    (table[2][2] == a or table[2][2] == b) and \
    not (table[0][0] == table[1][1] and table[1][1] == table[2][2]):
        # 성공
        return True
    
    # 오른쪽 위에서 왼쪽 아래 대각선 조사
    if (table[0][2] == a or table[0][2] == b) and \
    (table[1][1] == a or table[1][1] == b) and \
    (table[2][0] == a or table[2][0] == b) and \
    not (table[0][2] == table[1][1] and table[1][1] == table[2][0]):
        # 성공
        return True
    
    # 이외에는 실패
    return False

# can_win(a, b)
def can_win(a, b):

    # 가로, 세로, 대각선 중 하나라도 성공하면 성공
    return search_row(a, b) or search_col(a, b) or search_dia(a, b)        

# 설계
# win_cnt
win_cnt = 0

# 조합 구하기
for i in range(1, 9):
    for j in range(i+1, 10):
        # 2명이 한 팀이 되어 이길 수 있으면
        if can_win(str(i), str(j)):
            # win_cnt에 추가
            win_cnt += 1

# 출력
print(win_cnt)