n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 함수들
# vertical(k)
def vertical(k):

    # curr_line
    curr_line = []

    # points를 돌면서
    for x, y in points:
        # x좌표가 현재 수직 선분 내에 있는 점이면,
        if x == k:
            # curr_line에 추가
            curr_line.append((x, y))
    
    # curr_line 반환
    return curr_line

# parallel(k)
def parallel(k):
    
    # curr_line
    curr_line = []

    # points를 돌면서
    for x, y in points:
        # y좌표가 현재 수평 선분 내에 있는 점이면,
        if y == k:
            # curr_line에 추가
            curr_line.append((x, y))
    
    # curr_line 반환
    return curr_line

# search(a, b, c)
def search(a, b, c):
    
    # line_1, line_2, line_3
    line_1, line_2, line_3 = points_belongs_to_line[a], points_belongs_to_line[b], points_belongs_to_line[c]

    # curr_points_belongs_to_three_lines
    curr_points_belongs_to_three_lines = []

    # 첫번째 선분에서
    for point in line_1:
        # 겹치지 않은 점이면
        if point not in curr_points_belongs_to_three_lines:
            # curr_points_belongs_to_three_lines에 추가
            curr_points_belongs_to_three_lines.append(point)
    
    # 두번째 선분에서
    for point in line_2:
        # 겹치지 않은 점이면
        if point not in curr_points_belongs_to_three_lines:
            # curr_points_belongs_to_three_lines에 추가
            curr_points_belongs_to_three_lines.append(point)
    
    # 세번째 선분에서
    for point in line_3:
        # 겹치지 않은 점이면
        if point not in curr_points_belongs_to_three_lines:
            # curr_points_belongs_to_three_lines에 추가
            curr_points_belongs_to_three_lines.append(point)

    # 현재 세 개의 선분으로 포함하는 점들의 수를 반환
    return len(curr_points_belongs_to_three_lines)

# 설계
# points_belongs_to_line
points_belongs_to_line = []

# 모든 선분을 조사
for i in range(10):
    # 수직 선분을 조사
    points_belongs_to_line.append(vertical(i))
    # 수평 선분을 조사
    points_belongs_to_line.append(parallel(i))

# max_point_cnt
max_point_cnt = 0

# 선분 3개를 고르기
for i in range(8):
    for j in range(i+1, 9):
        for k in range(j+1, 10):
            # 겹치지 않는 선분을 탐색하여
            # max_point_cnt를 업데이트
            max_point_cnt = max(max_point_cnt, search(i, j, k))

# max_point_cnt가 n과 같다면
if max_point_cnt == n:
    print(1)
# 다르다면
else:
    print(0)