input = [(i.split('\n')) for i in open('day-1/input.txt', 'r').read().split('\n\n')]

m = []
for i in range(len(input)):
    elf = input[i]
    n = 0
    for j in range(len(elf)):
        cal = int(elf[j])
        n += cal
    m.append(n)



print(sum(sorted(m)[-3::]))