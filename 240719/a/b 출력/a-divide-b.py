n = input()
a = int(n.split()[0])
b = int(n.split()[1])

print(f'{a//b}.', end = "") #일의 자리

a %= b

for _ in range(20):
    a *= 10
    print(a//b, end = "")
    a %= b #나머지 곱하기 10을 b로 나눔