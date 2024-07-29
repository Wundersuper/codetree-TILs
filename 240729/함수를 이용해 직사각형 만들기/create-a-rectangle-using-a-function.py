def print_rec(n, m):
    for i in range(n):
        print('1' * m)


row_num, col_num = tuple(map(int, input().split()))

print_rec(row_num, col_num)