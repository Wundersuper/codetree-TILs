class Info:
    def __init__(self, name, height, weight):
        self.name = name
        self.h = height
        self.w = weight

arr = [tuple(input().split()) for _ in range(5)]
ppl = [
    Info(name, int(height), float(weight))
    for name, height, weight in arr
    ]

ppl.sort(key=lambda x: x.name)

print('name')
for p in ppl:
    print(p.name, p.h, p.w)

ppl.sort(key=lambda x: -x.h)

print()
print('height')
for p in ppl:
    print(p.name, p.h, p.w)