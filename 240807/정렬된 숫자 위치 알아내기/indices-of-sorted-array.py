class Number:
    def __init__(self, number, index):
        self.num, self.idx = number, index

N = int(input())

arr = list(map(int, input().split()))

numbers = []
for i in range(N):
    numbers.append(Number(arr[i], i+1))

numbers.sort(key=lambda x: x.num)

answer = [0] * (N+1)
for i, number in enumerate(numbers):
    answer[number.idx] = i+1

for a in answer[1:]:
    print(a, end = " ")