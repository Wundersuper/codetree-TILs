A = input()
A_math = int(A.split()[0])
A_eng = int(A.split()[1])

B = input()
B_math = int(B.split()[0])
B_eng = int(B.split()[1])

if A_math > B_math:
    print('A')
elif A_math == B_math and A_eng > B_eng:
    print('A')
else:
    print('B')