input = [[eval(j.strip()) for j in i.split('\n')] for i in open('day-13/input.txt', 'r').read().split('\n\n')]

def right_order(left, right):
    index = 0
    answer = None
    while answer == None:
        if index == len(left):
            if len(left) == len(right):
                break
            answer = True
        elif index == len(right):
            answer = False
        else:
            if isinstance(left[index], int) and isinstance(right[index], int):
                if left[index] > right[index]:
                    answer = False
                if left[index] < right[index]:
                    answer = True
            elif isinstance(left[index], list) and isinstance(right[index], int):
                answer = right_order(left[index], [right[index]])
            elif isinstance(left[index], int) and isinstance(right[index], list):
                answer = right_order([left[index]], right[index])
            else:
                answer = right_order(left[index], right[index])
            index += 1
    
    return answer

packets = []
for i in range(0, len(input), 1):
    pair = input[i]
    p1 = pair[0]
    p2 = pair[1]
    packets.append(p1)
    packets.append(p2)

from functools import cmp_to_key

c = 1
packets = sorted(packets, key=cmp_to_key(lambda x, y: -1 if right_order(x, y) else 1))
for i in range(len(packets)):
    packet = packets[i]
    if len(packet) == 1:
        if isinstance(packet[0], list) and len(packet[0]) == 1:
            if isinstance(packet[0][0], int):
                if packet[0][0] == 2 or packet[0][0] == 6:
                    c *= i + 1

print(c)