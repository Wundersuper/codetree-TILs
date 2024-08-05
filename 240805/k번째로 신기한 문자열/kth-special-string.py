inp = input().split()

n, k = int(inp[0]), int(inp[1])
T = inp[2]

word_list = [
    input()
    for _ in range(n)
]

target_word = []

for elem in word_list:
    if elem[0:len(T)] == T:
        target_word.append(elem)

target_word.sort()

print(target_word[k-1])