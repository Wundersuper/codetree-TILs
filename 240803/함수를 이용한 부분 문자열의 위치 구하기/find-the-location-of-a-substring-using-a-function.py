string = list(input())
target = list(input())
n1 = len(string)
n2 = len(target)


def is_part():
    for i in range(n1):
        for j in range(n2):
            if string[i:n1-n2+2] == target:
                start_idx = i
                return start_idx
    return -1


print(is_part())