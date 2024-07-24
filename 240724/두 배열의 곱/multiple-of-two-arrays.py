lst1 = []
lst2 = []
for _ in range(3):
    arr1 = list(map(int, input().split()))
    lst1.append(arr1)

input()

for _ in range(3):
    arr2 = list(map(int, input().split()))
    lst2.append(arr2)

sum_list = []
sum_val = 0
for i in range(3):
    lst3 = []
    for j in range(3):
        sum_val = lst1[i][j] * lst2[i][j]
        lst3.append(sum_val)
    sum_list.append(lst3)

for row in sum_list:
    for elem in row:
        print(elem, end = " ")
    print()