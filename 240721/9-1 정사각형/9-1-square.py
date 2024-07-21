n = int(input())
diff = 9

for i in range(n):
    for j in range(n):
        print(diff, end = "")
        diff -= 1
        if diff == 0:
            diff = 9
    print()