class Student:
    def __init__(self, height, weight, number):
        self.h = height
        self.w = weight
        self.n = number
    

N = int(input()) # 학생 수

students = []
for i in range(1, N+1):
    height, weight = map(int, input().split())
    students.append(Student(height, weight, i))

students.sort(key=lambda x: (x.h, -x.w))

for s in students:
    print(s.h, s.w, s.n)