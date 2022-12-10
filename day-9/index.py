input = [([i.split(' ')[0], int(i.split(' ')[1])]) for i in open('day-9/input.txt', 'r').read().split('\n')]

hits = [(0, 0)]
rope_len = 10
rope = []
for i in range(rope_len):
    rope.append([0, 0])

for i in range(0, len(input), 1):
    d, c = input[i]
    for _ in range(c):
        if d == 'R':
            rope[0][0] += 1
        if d == 'L':
            rope[0][0] -= 1
        if d == 'U':
            rope[0][1] += 1
        if d == 'D':
            rope[0][1] -= 1
        
        for p in range(1, rope_len):
            if rope[p - 1][0] - rope[p][0] == 2:
                rope[p][0] += 1
                if rope[p - 1][1] < rope[p][1]:
                    rope[p][1] -= 1
                if rope[p - 1][1] > rope[p][1]:
                    rope[p][1] += 1
                if p == rope_len - 1:
                    hits.append((rope[p][0], rope[p][1]))
            if rope[p - 1][0] - rope[p][0] == -2:
                rope[p][0] -= 1
                if rope[p - 1][1] < rope[p][1]:
                    rope[p][1] -= 1
                if rope[p - 1][1] > rope[p][1]:
                    rope[p][1] += 1
                if p == rope_len - 1:
                    hits.append((rope[p][0], rope[p][1]))
            
            if rope[p - 1][1] - rope[p][1] == 2:
                rope[p][1] += 1
                if rope[p - 1][0] < rope[p][0]:
                    rope[p][0] -= 1
                if rope[p - 1][0] > rope[p][0]:
                    rope[p][0] += 1
                if p == rope_len - 1:
                    hits.append((rope[p][0], rope[p][1]))
            if rope[p - 1][1] - rope[p][1] == -2:
                rope[p][1] -= 1
                if rope[p - 1][0] < rope[p][0]:
                    rope[p][0] -= 1
                if rope[p - 1][0] > rope[p][0]:
                    rope[p][0] += 1
                if p == rope_len - 1:
                    hits.append((rope[p][0], rope[p][1]))

print(len(set(hits)))