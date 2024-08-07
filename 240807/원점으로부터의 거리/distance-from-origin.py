class Dot:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.num = number

N = int(input()) # 점의 수

dots = []
for i in range(1, N+1):
    x, y = tuple(map(int, input().split()))
    dots.append(Dot(x, y, i))

dots.sort(key = lambda x: ((abs(x.x - 0) + abs(x.y - 0)), x.num))

for d in dots:
    print(d.num)