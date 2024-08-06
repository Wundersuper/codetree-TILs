class Body:
    def __init__(self, name, height, weight):
        self.name = name
        self.h = height
        self.w = weight


n = int(input())

arr = [tuple(input().split()) for _ in range(n)]
body = [Body(name, int(height), int(weight)) for name, height, weight in arr]

body.sort(key = lambda x: x.h)

for person in body:
    print(person.name, person.h, person.w)