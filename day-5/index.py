input = [(i) for i in open('day-5/input.txt', 'r').read().split('\n\n')]

buckets = {}

bc = 9

for i in range(bc):
    buckets[i + 1] = []

for line in input[0].split('\n'):
    for i in range(bc):
        if(not line[i * 4 + 1] == ' '):
            buckets[i + 1].insert(0, line[i * 4 + 1])

for i in range(bc):
    buckets[i + 1] = buckets[i + 1][1::]

for i in input[1].split('\n'):
    line = i.split(' ')

    c = int(line[1])
    s = int(line[3])
    e = int(line[5])

    for j in buckets[s][-c::]:
        buckets[e].append(j)
    buckets[s] = buckets[s][0:-c]

f = ''
for i in range(bc):
    f += str(buckets[i + 1][-1])

print(f)