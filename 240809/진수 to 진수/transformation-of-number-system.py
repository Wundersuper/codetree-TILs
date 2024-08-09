a, b = tuple(map(int, input().split()))
n = list(map(int, input()))

num = 0
for i in range(len(n)):
    num = num * a + n[i]

digits = []
while True:
    if num < b:
        digits.append(num)
        break
    
    digits.append(num % b)
    num //= b

for elem in digits[::-1]:
    print(elem, end = "")