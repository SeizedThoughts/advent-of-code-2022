input = [([[int(k) for k in j.split(',')] for j in i.split(' -> ')]) for i in open('day-14/input.txt', 'r').read().split('\n')]

min_x = -1
max_x = -1
max_y = -1

for i in range(0, len(input), 1):
    line = input[i]
    for j in line:
        if j[0] > max_x:
            max_x = j[0]
        if min_x == -1 or j[0] < min_x:
            min_x = j[0]
        if j[1] > max_y:
            max_y = j[1]

out = [list('.' * (max_x - min_x + 3 + 2 * (max_y + 3))) for _ in range(max_y + 3)]

input.append([[min_x - 1 - (max_y + 3), max_y + 2], [max_x + 1 + max_y + 3, max_y + 2]])

cursor = [-1, -1]
cursor2 = [-1, -1]
for i in range(0, len(input), 1):
    line = input[i]
    cursor2[0] = line[0][1]
    cursor2[1] = line[0][0] - min_x + 1 + max_y + 3
    out[cursor2[0]][cursor2[1]] = '#'
    for j in range(1, len(line)):
        cursor[0] = cursor2[0]
        cursor[1] = cursor2[1]
        cursor2[0] = line[j][1]
        cursor2[1] = line[j][0] - min_x + 1 + max_y + 3
        if cursor2[0] > cursor[0]:
            for k in range(cursor2[0] - cursor[0]):
                cursor[0] += 1
                out[cursor[0]][cursor[1]] = '#'
        if cursor2[0] < cursor[0]:
            for k in range(cursor[0] - cursor2[0]):
                cursor[0] -= 1
                out[cursor[0]][cursor[1]] = '#'
        if cursor2[1] > cursor[1]:
            for k in range(cursor2[1] - cursor[1]):
                cursor[1] += 1
                out[cursor[0]][cursor[1]] = '#'
        if cursor2[1] < cursor[1]:
            for k in range(cursor[1] - cursor2[1]):
                cursor[1] -= 1
                out[cursor[0]][cursor[1]] = '#'

count = 0
done = False
coords = [-1, -1]
while not done:
    coords[0] = 0
    coords[1] = 500 - min_x + 1 + max_y + 3
    headed = [coords[0], coords[1]]
    while out[headed[0]][headed[1]] == '.':
        coords[0] = headed[0]
        coords[1] = headed[1]
        headed[0] += 1
        try:
            if out[headed[0]][headed[1]] != '.':
                if out[headed[0]][headed[1] - 1] == '.':
                    headed[1] -= 1
                elif out[headed[0]][headed[1] + 1] == '.':
                    headed[1] += 1
        except:
            done = True
            break
    if not done:
        count += 1
        out[coords[0]][coords[1]] = 'o'

    if coords[0] == 0:
        break


# for i in out:
#     t = ''
#     for c in i:
#         t += c
#     print(t)

print(count)