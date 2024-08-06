class Student:
    def __init__(self, name, fach1, fach2, fach3):
        self.name = name
        self.f1 = fach1
        self.f2 = fach2
        self.f3 = fach3

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
students = [
    Student(name, int(fach1), int(fach2), int(fach3))
    for name, fach1, fach2, fach3 in arr
]

students.sort(key=lambda x: x.f1 + x.f2 + x.f3)

for s in students:
    print(s.name, s.f1, s.f2, s.f3)