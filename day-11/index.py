input = [(i.split('\n')) for i in open('day-11/input.txt', 'r').read().split('\n\n')]

monkeys = []

for i in range(0, len(input), 1):
    monkey = input[i]
    monkeys.append({
        'items': [int(i) for i in monkey[1].split(': ')[1].split(', ')],
        'operation': monkey[2].split(': new = ')[1],
        'test': int(monkey[3].split(': divisible by ')[1]),
        'test_true': int(monkey[4].split(': throw to monkey ')[1]),
        'test_false': int(monkey[5].split(': throw to monkey ')[1]),
        'inspections': 0
    })

primes = [monkey['test'] for monkey in monkeys]

for monkey in monkeys:
    monkey['items'] = [[i % p for p in primes] for i in monkey['items']]

rounds = 10000
for round in range(1, rounds + 1):
    for m in range(len(monkeys)):
        monkey = monkeys[m]
        for i in range(len(monkey['items'])):
            monkey['items'][i] = [int(eval(str(monkey['items'][i][d]).join(monkey['operation'].split('old')))) % primes[d] for d in range(len(monkey['items'][i]))]
            if monkey['items'][i][m] == 0:
                monkeys[monkey['test_true']]['items'].append(monkey['items'][i])
            else:
                monkeys[monkey['test_false']]['items'].append(monkey['items'][i])
            monkey['inspections'] += 1
        monkey['items'] = []

inspects = sorted([monkey['inspections'] for monkey in monkeys])

print(inspects[-2] * inspects[-1])