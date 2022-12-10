input = [(i.split(' ')) for i in open('day-10/input.txt', 'r').read().split('\n')]

x = 1
c = 1
row = ''
for i in range(0, len(input), 1):
    line = input[i]

    if x - 1 <= c - 1 and x + 1 >= c - 1:
        row += '#'
    else:
        row += '.'
    
    if len(line) == 1:
        if c % 40 == 0:
            c = 0
            print(row)
            row = ''
        c += 1
        continue

    if c % 40 == 0:
        c = 0
        print(row)
        row = ''
    c += 1

    if x - 1 <= c - 1 and x + 1 >= c - 1:
        row += '#'
    else:
        row += '.'

    x += int(line[1])
    
    if c % 40 == 0:
        c = 0
        print(row)
        row = ''
    c += 1