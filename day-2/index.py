input = [(i) for i in open('day-2/input.txt', 'r').read().split('\n')]

score = 0
for i in range(len(input)):
    line = input[i]
    tt = line[0]
    mt = line[2]
    if(mt == 'X'):
        mt = 1
    if(mt == 'Y'):
        mt = 2
    if(mt == 'Z'):
        mt = 3

    if(tt == 'A'):
        tt = 1
    if(tt == 'B'):
        tt = 2
    if(tt == 'C'):
        tt = 3

    if(mt == 1):
        score += ((tt + 1) % 3) + 1
    if(mt == 2):
        score += 3
        score += tt
    if(mt == 3):
        score += 6
        score += (tt % 3) + 1

print(score)