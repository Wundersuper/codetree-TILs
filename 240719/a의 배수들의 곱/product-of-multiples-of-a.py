a, b = map(int, input().split())

prod = 1
for i in range(1, b+1):
    if i >= a and i % a == 0:
        prod *= i
    
print(prod)