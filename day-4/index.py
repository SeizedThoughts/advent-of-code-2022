input = [([[int(k) for k in j.split('-')] for j in i.split(',')]) for i in open('day-4/input.txt', 'r').read().split('\n')]

tot = 0
for i in range(len(input)):
    l, r = input[i]
    if((l[0] <= r[0] and l[1] >= r[0]) or (r[0] <= l[0] and r[1] >= l[0])):
        tot += 1

print(tot)