n, b = tuple(map(int, input().split()))
price_list = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


def discount(idx):
    p1, s1 = price_list[idx]

    return p1 // 2 + s1


def simulate(curr_list):
    curr_list.sort()

    for i in range(1, n):
        if sum(curr_list[:i+1]) > b:
            return i


max_students = 0
for i in range(n):
    merged_price = []
    for j in range(n):
        if i == j:
            merged_price.append(discount(j))
        else:
            p1, s1 = price_list[j]
            merged_price.append(p1 + s1)

    max_students = max(max_students, simulate(merged_price))

print(max_students)