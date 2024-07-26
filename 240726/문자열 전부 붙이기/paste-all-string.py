n = int(input())

string = [
    input()
    for _ in range(n)
]

result = ""

for elem in string:
    result += elem

print(result)