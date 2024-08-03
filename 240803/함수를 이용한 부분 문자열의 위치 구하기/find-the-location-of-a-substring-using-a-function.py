string = list(input())
target = list(input())
n1 = len(string)
n2 = len(target)


def is_part():
    for i in range(n1):
        if string[i:n1-n2+2] == target:
            start_idx = i
            return start_idx
        if n1 - i - n2 < 0:
            return -1


print(is_part())