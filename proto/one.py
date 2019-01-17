from proto.util import *

data, _ = load()

scan(data, 0, 10)
# scan(data, 5, 1000)

good, _ = load(bank_mapper)

show(good, 10)
shuffle(good)

size = 1000
test = good[:size]
train = good[size:]

success = 0
statics = {'passP': 0, 'failP': 0, 'passN': 0, 'failN': 0}
for one in test:
    neighbours = []
    minDist = 8
    for two in train:
        cnt = 7
        for index in range(7):
            if two[index] == one[index]:
                cnt -= 1
        if cnt < minDist:
            minDist = cnt
            neighbours.clear()
            neighbours.append(two)
        elif cnt == minDist:
            neighbours.append(two)
    count = 0
    for line in neighbours:
        if line[7] == '"yes"':
            count += 1
    rate = count / len(neighbours)
    desc = "error"
    if rate > 0.5:
        if one[7] == '"yes"':
            desc = 'passP'
        else:
            desc = 'failP'
    else:
        if one[7] == '"yes"':
            desc = 'failN'
        else:
            desc = 'passN'
    statics[desc] += 1

    if desc != 'passN':
        print(f'dist {minDist} with {len(neighbours)} {desc} yesRate={rate}')

    if (rate > 0.5 and one[7] == '"yes"') or (rate < 0.5 and one[7] == '"no"'):
        success += 1
    # print(neighbours)

print(f'{success} in {len(test)}')
print(statics)
