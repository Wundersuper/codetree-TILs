n = int(input())

line = [0 for _ in range(203)]
start = 101

for i in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        for j in range(1, x+1):
            line[start - j] += 1
        start -= x
    else:
        for j in range(x):
            line[start + j] += 1
        start += x

count = 0
for i in range(len(line)):
    if line[i] >= 2:
        count += 1

print(count)