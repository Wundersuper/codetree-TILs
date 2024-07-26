n = int(input())

string = input()
string2 = ""

for char in string:
    if char != " ":
        string2 += char

cnt = 0
for elem in string2:
    print(elem, end = "")
    cnt += 1
    if cnt % 5 == 0:
        print()