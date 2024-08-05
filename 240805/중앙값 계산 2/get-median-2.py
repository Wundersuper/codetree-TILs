n = int(input())

nums = list(map(int, input().split()))


def find_mid(n):
    global nums

    arr = []
    median = []
    for i in range(n):
        arr.append(nums[i])
        
        if i % 2 == 0:
            arr.sort()
            median.append(arr[i // 2])
    
    for elem in median:
        print(elem, end = " ") 


find_mid(n)