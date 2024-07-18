n1 = input()
n1_age = int(n1.split()[0])
n1_sex = n1.split()[1]

n2 = input()
n2_age = int(n2.split()[0])
n2_sex = n2.split()[1]

if (n1_age >= 19 and n1_sex == 'M') or (n2_age >= 19 and n2_sex == 'M'):
    print(1)
else:
    print(0)