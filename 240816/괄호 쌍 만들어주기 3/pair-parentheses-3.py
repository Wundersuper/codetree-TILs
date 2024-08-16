string = list(input())

ans = 0
for i in range(len(string)):
    for j in string[i:]:
        if string[i] + j == '()':
            ans += 1

print(ans)