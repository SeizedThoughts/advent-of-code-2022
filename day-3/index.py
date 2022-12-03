input = [(i) for i in open('day-3/input.txt', 'r').read().split('\n')]


sum = 0

for i in range(len(input)):
    if(i % 3 == 0):
        line1 = input[i]
        line2 = input[i + 1]
        line3 = input[i + 2]

        for item in list(set(list(line1)).intersection(set(list(line2))).intersection(set(list(line3)))):
            if(item.lower() == item):
                sum += ord(item) - ord('a') + 1
            else:
                sum += ord(item) - ord('A') + 27

    

print(sum)