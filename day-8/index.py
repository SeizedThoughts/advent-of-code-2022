input = [([int(j) for j in i]) for i in open('day-8/input.txt', 'r').read().split('\n')]

best = 0
for i in range(1, len(input) - 1, 1):
    for j in range(1, len(input[0]) - 1, 1):
        tile = input[i][j]

        di = i + 1
        ds = 0
        while(di < len(input)):
            if(tile > input[di][j]):
                ds += 1
            else:
                ds += 1
                break
            di += 1

        ui = i - 1
        us = 0
        while(ui >= 0):
            if(tile > input[ui][j]):
                us += 1
            else:
                us += 1
                break
            ui -= 1

        rj = j + 1
        rs = 0
        while(rj < len(input[0])):
            if(tile > input[i][rj]):
                rs += 1
            else:
                rs += 1
                break
            rj += 1

        lj = j - 1
        ls = 0
        while(lj >= 0):
            if(tile > input[i][lj]):
                ls += 1
            else:
                ls += 1
                break
            lj -= 1
        
        s = us * ls * rs * ds
        if(s > best):
            best = s

print(best)