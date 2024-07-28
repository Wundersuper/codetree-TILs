A = input()
B = input() #명령 문자열

lst_B = list(B)
len_B = len(lst_B)

for i in range(len_B):
    if lst_B[i] == 'L':
        A = A[1:] + A[0]

    else:
        A = A[-1] + A[:-1]

print(A)