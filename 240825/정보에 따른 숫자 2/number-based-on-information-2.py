# t, a, b 입력
t, a, b = map(int, input().split())
# linear
linear = [0] * 1001
# c, x 입력
for _ in range(t):
    c, x = input().split()
    linear[int(x)] = c

# 함수들
# get_most_close_s(idx)
def get_most_close_s(idx):
    
    # s_idx_list
    s_idx_list = list()

    # linear 탐색
    for i in range(1001):
        # S를 찾으면,
        if linear[i] == 'S':
            # 인덱스를 기록
            s_idx_list.append(i)
    
    # min_dist
    min_dist = sys.maxsize

    # 각 인덱스와의 차이를 구해가며
    for s_idx in s_idx_list:
        # min_dist 업데이트
        min_dist = min(min_dist, abs(s_idx - idx))
    
    # min_dist 반환
    return min_dist

# get_most_close_n(idx)
def get_most_close_n(idx):
    
    # n_idx_list
    n_idx_list = list()

    # linear 탐색
    for i in range(1001):
        # N을 찾으면,
        if linear[i] == 'N':
            # 인덱스를 기록
            n_idx_list.append(i)
    
    # min_dist
    min_dist = sys.maxsize

    # 각 인덱스와의 차이를 구해가며
    for n_idx in n_idx_list:
        # min_dist 업데이트
        min_dist = min(min_dist, abs(n_idx - idx))
    
    # min_dist 반환
    return min_dist

# 설계
import sys

# special_pos_cnt
special_pos_cnt = 0

# 완전 탐색 시작
for i in range(a, b+1):
    
    # d1, d2
    d1, d2 = get_most_close_s(i), get_most_close_n(i)

    # d1이 d2보다 같거나 작은 경우
    if d1 <= d2:
        # special_pos_cnt 올려주기
        special_pos_cnt += 1

# 출력
print(special_pos_cnt)