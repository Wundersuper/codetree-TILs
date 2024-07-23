n, q = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

for i in range(q):
    qna = list(map(int, input().split()))

    if qna[0] == 1:
        print(arr[qna[1] - 1])
    elif qna[0] == 2:
        if qna[1] in arr:
            for elem in arr:
                print(arr.index(qna[1])+1)
                break
        else:
            print("0")
    else:
        for i in range(qna[1]-1, qna[2]):
            print(arr[i], end = " ")
        print()