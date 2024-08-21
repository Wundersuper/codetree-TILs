# n 입력
n = int(input())
# conditions
conditions = []
# conditions 입력
for _ in range(n):
    num, cnt_1, cnt_2 = input().split()
    # 형 변환
    cnt_1, cnt_2 = int(cnt_1), int(cnt_2)
    conditions.append([num, cnt_1, cnt_2])

# 함수들
# cnt_2_is_ok(k, correct_cnt, a, b, c)
def cnt_2_is_ok(k, correct_cnt, a, b, c):

    # curr_cnt
    curr_cnt = 0

    # k 분해
    a1, b1, c1 = int(k[0]), int(k[1]), int(k[2])

    # 비교
    if a1 == b or a1 == c:
        curr_cnt += 1
    if b1 == a or b1 == c:
        curr_cnt += 1
    if c1 == a or c1 == b:
        curr_cnt += 1
    
    # cnt_2과 조건이 맞는지 비교
    return curr_cnt == correct_cnt

# cnt_1_is_ok(k, correct_cnt, a, b, c)
def cnt_1_is_ok(k, correct_cnt, a, b, c):
    
    # curr_cnt
    curr_cnt = 0

    # k 분해
    a1, b1, c1 = int(k[0]), int(k[1]), int(k[2])

    # 비교
    if a1 == a:
        curr_cnt += 1
    if b1 == b:
        curr_cnt += 1
    if c1 == c:
        curr_cnt += 1
    
    # cnt_1과 조건이 맞는지 비교
    return curr_cnt == correct_cnt

# is_ok
def is_ok(con, a, b, c):
    # cnt_1과 cnt_2 조건 맞는지 확인
    return cnt_1_is_ok(con[0], con[1], a, b, c) and cnt_2_is_ok(con[0], con[2], a, b, c)

# everything_is_ok(a, b, c)
def everything_is_ok(a, b, c):
    
    # 모든 조건 탐색
    for condition in conditions:
        # 한번이라도 조건에 맞지 않으면,
        if not is_ok(condition, a, b, c):
            # 실패
            return False
    
    # 모든 조건을 통과하면 성공
    return True

# 설계
# ans
ans = 0

# 완전 탐색 시작
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            # 서로 다른 수라면,
            if i != j and j != k and i != k:
                # 조건을 모두 통과하였으면,
                if everything_is_ok(i,j,k):
                    # 유추 가능성이 있음
                    ans += 1

# 출력
print(ans)