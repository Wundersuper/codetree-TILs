n = int(input())
arr = list(map(int, input().split()))
max1 = n

while True:
    max2 = 0
    for j in range(1,max1):
        if  arr[max2] < arr[j]:
            max2 = j
    print(max2 + 1,end=' ')

    if  max2 == 0 :
        break
    
    max1 = max2