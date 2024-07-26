A = input()

string = ''

curr_char = A[0]
cnt = 1

for target_char in A[1:]:
    if target_char == curr_char:
        cnt += 1
    else:
        string += curr_char
        string += str(cnt)

        curr_char = target_char
        cnt = 1

string += curr_char
string += str(cnt)

print(len(string))
print(string)