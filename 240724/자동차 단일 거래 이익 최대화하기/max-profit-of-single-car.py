n = int(input())

price = list(map(int, input().split()))

max_cost = 1
for i in range(n-1, 0, -1):
    for j in range(i):
        plus = price[i] - price[j]
        if max_cost < plus:
            max_cost = plus
        
if max_cost < 0:
    print('0')
else:
    print(max_cost)