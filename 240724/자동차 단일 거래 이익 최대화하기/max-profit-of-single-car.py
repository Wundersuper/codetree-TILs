n = int(input())

price = list(map(int, input().split()))

max_profit = 0

for i in range(n):
    for j in range(i+1, n):
        profit = price[j] - price[i]

        if max_profit < profit:
            max_profit = profit

print(max_profit)