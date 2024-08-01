a, b = tuple(map(int, input().split()))


def all_even(n):
    return (n // 10 + n % 10) % 2 == 0

def is_prime(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    
    if cnt == 2:
        return True

sum_val = 0
for i in range(a, b+1):
    if is_prime(i) and all_even(i):
        sum_val += 1

print(sum_val)