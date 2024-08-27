# n 입력
n = int(input())
# point_pos
point_pos = list()
# x, y 입력
for _ in range(n):
    point_pos.append(tuple(map(int, input().split())))

# 함수들
# get_q1(x, y)
def get_q1(x, y):
    
    # point_cnt
    point_cnt = 0
    
    # point_pos를 돌면서
    for point in point_pos:
        # unpacking
        p_x, p_y = point
        
        # 1사분면에 위치해 있으면
        if p_x > x and p_y > y:
            # point_cnt 올려주기
            point_cnt += 1
    
    # 반환
    return point_cnt

# get_q2(x, y)
def get_q2(x, y):
    
    # point_cnt
    point_cnt = 0
    
    # point_pos를 돌면서
    for point in point_pos:
        # unpacking
        p_x, p_y = point
        
        # 2사분면에 위치해 있으면
        if p_x < x and p_y > y:
            # point_cnt 올려주기
            point_cnt += 1
    
    # 반환
    return point_cnt

# get_q3(x, y)
def get_q3(x, y):
    
    # point_cnt
    point_cnt = 0
    
    # point_pos를 돌면서
    for point in point_pos:
        # unpacking
        p_x, p_y = point
        
        # 3사분면에 위치해 있으면
        if p_x < x and p_y < y:
            # point_cnt 올려주기
            point_cnt += 1
    
    # 반환
    return point_cnt

# get_q4(x, y)
def get_q4(x, y):
    
    # point_cnt
    point_cnt = 0
    
    # point_pos를 돌면서
    for point in point_pos:
        # unpacking
        p_x, p_y = point
        
        # 4사분면에 위치해 있으면
        if p_x > x and p_y < y:
            # point_cnt 올려주기
            point_cnt += 1
    
    # 반환
    return point_cnt


# 설계
# min_points
import sys
min_points = sys.maxsize

# 완전 탐색 시작 -> 모든 경계선을 탐색
for i in range(2, 101, 2):
    for j in range(2, 101, 2):
        
        # q1, q2, q3, q4 -> 경계선을 기준으로 각 사분면에 위치한 점의 갯수
        q1, q2, q3, q4 = get_q1(i, j), get_q2(i, j), get_q3(i, j), get_q4(i, j)
        # curr_max_points
        curr_max_points = max(q1, q2, q3, q4)
        # min_points update
        min_points = min(min_points, curr_max_points)

# 출력
print(min_points)