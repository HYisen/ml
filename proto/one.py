from random import shuffle

data = []
name = []
age = []


def scan(data, col, step):
    stat = {12: 100}
    for attr in [row[col] for row in data]:
        # print(attr)
        cls = int(int(attr) / step)
        # print(cls)
        if cls not in stat:
            stat[cls] = 0
        stat[cls] += 1
    for key in sorted(stat):
        print(f'{key:3d}:{stat[key]:5d}')


def show(data, limit=0):
    for index, row in enumerate(data):
        if limit != 0 and index >= limit:
            break
        print(row)


with open('../data/bank.csv') as fp:
    for linage, line in enumerate(fp):
        split = line.split(';')
        if linage == 0:
            name = split
            continue
        print(f'{linage} => {line}')
        data.append(split)
        age.append(split[0])

d = {}
for i in range(8):
    col = []
    for line in data:
        col.append(line[i])
    # print(f'{name[i]}=>{col}\n')
    d[name[i]] = col

# scan(data, 0, 10)
# scan(data, 5, 1000)

good = []

for line in data:
    left = [line[k] for k in range(8)]
    item = int(line[0])
    if item < 30:
        left[0] = "below"
    elif item < 40:
        left[0] = "30s"
    elif item < 50:
        left[0] = "40s"
    else:
        left[0] = "above"

    item = int(line[5])
    if item < 0:
        left[5] = "minus"
    elif item < 1000:
        left[5] = "low"
    else:
        left[5] = "high"

    good.append(left)

# for attr in [line[2] for line in data]:
#     print(attr)

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
