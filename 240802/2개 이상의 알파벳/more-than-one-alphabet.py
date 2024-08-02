A = input()


def is_different(string):
    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            return True
    
    return False


if is_different(A):
    print('Yes')
else:
    print('No')