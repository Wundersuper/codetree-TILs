a = input()
a_cold = a.split()[0]
a_temp = int(a.split()[1])

b = input()
b_cold = b.split()[0]
b_temp = int(b.split()[1])

c = input()
c_cold = c.split()[0]
c_temp = int(c.split()[1])

if a_cold == 'Y' and a_temp >= 37:
    if (b_cold == 'Y' and b_temp >= 37) or (c_cold == 'Y' and c_temp >= 37):
        print('E')
    else:
        print('N')
elif (b_cold == 'Y' and b_temp >= 37) and (c_cold == 'Y' and c_temp >= 37):
    print('E')
else:
    print('N')