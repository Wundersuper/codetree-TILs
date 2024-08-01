import sys

n1, n2 = tuple(map(int, input().split())) #A, B 원소 개수

A = list(map(int, input().split()))
B = list(map(int, input().split()))


def is_part(a, b):
    for i in range(a):
        success = True

        for j in range(b):
            if i + j >= a:
                success = False
                break

            if A[i+j] != B[j]:
                success = False
                break
            
        if success:
            print('Yes')
            sys.exit()

    print('No')

is_part(n1, n2)