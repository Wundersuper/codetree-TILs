class Info:
    def __init__(self, name, height, weight):
        self.name = name
        self.h = height
        self.w = weight
    

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
ppl = [
    Info(name, int(height), int(weight))
    for name, height, weight in arr
]

ppl.sort(key = lambda x: (x.h, -x.w))

for p in ppl:
    print(p.name, p.h, p.w)