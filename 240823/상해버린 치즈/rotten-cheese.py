# N, M, D, S 입력
N, M, D, S = map(int, input().split())

# time_table
time_table = []

# time_table 채우기
for _ in range(D):
    time_table.append(tuple(map(int, input().split())))

# sick_time
sick_time = []

# sick_time 채우기
for _ in range(S):
    sick_time.append(tuple(map(int, input().split())))

# 함수들
# find_eaten_cheese(person, time)
def find_eaten_cheese(person, time):
    
    # curr_cheese
    curr_cheese = []

    # time_table에서
    for i in range(D):
        
        # unpacking
        p, m, t = time_table[i]

        # 해당 사람이 아프기 전에 먹은 치즈라면
        if p == person and t < time:

            # curr_cheese에 추가
            curr_cheese.append(m)
    
    # 반환
    return curr_cheese

# is_common_cheese(cheese)
def is_common_cheese(cheese):

    # eaten_cheese에 있는 모든 리스트에
    for cheese_list in eaten_cheese:
        # 한번이라도 현재 치즈가 없으면
        if cheese not in cheese_list:
            # 실패
            return False
    
    # 모든 검사를 통과하면 True
    return True

# count_people(cheese)
def count_people(cheese):
    
    # curr_people
    curr_people = []

    # time_table을 돌며
    for i in range(D):
        
        # unpacking
        p, m, t = time_table[i]

        # 현재 치즈를 먹은 사람을 찾으면
        if m == cheese and p not in curr_people:
            # curr_people에 추가
            curr_people.append(p)
    
    # 반환
    return len(curr_people)

# 설계
# eaten_cheese
eaten_cheese = []

# sick_time 기준으로 탐색 시작
for i in range(S):
    
    # unpacking
    person, time = sick_time[i]

    # eaten_cheese에 
    # 아픈 사람이 아프기 1초전까지 먹은 치즈를 리스트 형태로 추가
    eaten_cheese.append(find_eaten_cheese(person, time))

# common_cheese -> 공통적으로 먹은 치즈
common_cheese = []

for cheese in eaten_cheese[0]:
    # 현재 치즈가 공통 치즈이면
    if is_common_cheese(cheese):
        # common_cheese에 추가
        common_cheese.append(cheese)

# max_people -> 공통적으로 먹은 치즈를 먹은 사람의 최댓값
max_people = 0

# 공통적으로 먹은 치즈를 하나씩 조사하며
for cheese in common_cheese:
    
    # max_people 업데이트
    max_people = max(max_people, count_people(cheese))

# 출력
print(max_people)