N = int(input())


def num_sum(n):
    if n < 2:
        return 1
    
    return num_sum(n-1) + n


print(num_sum(N))