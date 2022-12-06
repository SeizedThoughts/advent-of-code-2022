input = open('day-6/input.txt', 'r').read()


l = ''
for i in range(len(input)):
    l += input[i]
    if i < 14:
        continue
    l = l[1::]
    if len(list(l)) == len(list(set(list(l)))):
        print(i + 1)
        break