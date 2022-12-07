input = [(i) for i in open('day-7/input.txt', 'r').read().split('\n')]

path = []
fs = {}
cd = fs
i = 0
while(i < len(input)):
    line = input[i]
    if line[0:4] == '$ cd':
        if line[5] == '/':
            cd = fs
            path = []
        elif line[5::] == '..':
            cd = fs
            path = path[0:-1]
            for part in path:
                cd = cd[part]
        else:
            if not line[5::] + '.dir' in cd.keys():
                cd[line[5::] + '.dir'] = {}
            cd = cd[line[5::] + '.dir']
            path.append(line[5::] + '.dir')
    if line == '$ ls':
        i += 1
        while(i < len(input) and not input[i][0] == '$'):
            parts = input[i].split(' ')
            if parts[0] == 'dir':
                cd[parts[1] + '.dir'] = {}
            else:
                cd[parts[1]] = int(parts[0])
            i += 1
        i -= 1
    i += 1

def size(dir):
    tot = 0
    for file in dir.keys():
        if file[-4::] == '.dir':
            tot += size(dir[file])
        else:
            tot += dir[file]
    return tot

def lol(dir):
    tot = 0
    for file in dir.keys():
        if file[-4::] == '.dir':
            tot += lol(dir[file])
            s = size(dir[file])
            if s <= 100000:
                tot += s
    
    return tot

space = 70000000 - size(fs)
space_needed = 30000000 - space

def find_smallest(dir):
    smallest = size(dir)
    for file in dir.keys():
        if file[-4::] == '.dir':
            b =  find_smallest(dir[file])
            
            if b < smallest and b >= space_needed:
                smallest = b
    
    return smallest

print(find_smallest(fs))