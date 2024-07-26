string = input()
n = int(input())

leng = len(string)
if leng < n:
    for i in range(leng-1, -1, -1):
        print(string[i], end = "")
else:
    for i in range(leng-1, leng-n-1, -1):
        print(string[i], end = "")