arr = list(map(int, input().split()))

max_val, min_val = 1, 1000 

for elem in arr:
    if elem < 500:
        if elem > max_val:
            max_val = elem
    
    if elem > 500:
        if min_val > elem:
            min_val = elem

print(max_val, min_val)