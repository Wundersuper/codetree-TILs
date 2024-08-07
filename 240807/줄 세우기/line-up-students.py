class Student:
    def __init__(self, height, weight, number):
        self.h = height
        self.w = weight
        self.n = number

N = int(input()) #학생 수

students = []

for _ in range(N):
    height, weight = tuple(map(int, input().split()))
    students.append(Student(height, weight, _))

students.sort(key=lambda x: (-x.h, -x.w, x.n))

for s in students:
    print(s.h, s.w, s.n + 1)