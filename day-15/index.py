input = [([[int(k) for k in j.split(', y=')] for j in i.split('Sensor at x=')[1].split(': closest beacon is at x=')]) for i in open('day-15/input.txt', 'r').read().split('\n')]

for i in range(0, len(input), 1):
    line = input[i]
    line[1] = abs(line[0][0] - line[1][0]) + abs(line[0][1] - line[1][1])

overlaps = []
lines = []
for s in input:
    line = (1, s[0][1] - (s[0][0] + (s[1] + 1)))
    if not line in lines:
        lines.append(line)
    else:
        if not line in overlaps:
            overlaps.append(line)
    line = (1, s[0][1] - (s[0][0] - (s[1] + 1)))
    if not line in lines:
        lines.append(line)
    else:
        if not line in overlaps:
            overlaps.append(line)
    line = (-1, s[0][1] + (s[0][0] + (s[1] + 1)))
    if not line in lines:
        lines.append(line)
    else:
        if not line in overlaps:
            overlaps.append(line)
    line = (-1, s[0][1] + (s[0][0] - (s[1] + 1)))
    if not line in lines:
        lines.append(line)
    else:
        if not line in overlaps:
            overlaps.append(line)

hits = []
for line1 in lines:
    for line2 in lines:
        if line1[0] == line2[0]:
            continue
        else:
            hit = (int((line2[1] - line1[1]) / (line1[0] - line2[0])), int((line2[1] - line1[1]) / (line1[0] - line2[0]) * line1[0] + line1[1]))
            if hit not in hits:
                hits.append(hit)

max = 4000000
for x, y in hits:
    if x < 0 or y < 0 or x > max or y > max:
        continue
    f = True
    for line in input:
        if abs(x - line[0][0]) + abs(y - line[0][1]) <= line[1]:
            f = False
            break
    if f:
        print(x * 4000000 + y)