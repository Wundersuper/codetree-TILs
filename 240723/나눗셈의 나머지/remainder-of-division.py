a, b = map(int, input().split())

count_arr = [0] * b

while True:
    if a <= 1:
        break
    count_arr[a % b] += 1
    a //= b
    
sum_val = 0
for i in range(b):
    sum_val += (count_arr[i] ** 2)

print(sum_val)