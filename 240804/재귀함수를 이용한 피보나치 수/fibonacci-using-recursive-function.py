N = int(input())


def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    return Fibonacci(n-2) + Fibonacci(n-1)


print(Fibonacci(N))