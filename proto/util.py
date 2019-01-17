import random


def echo():
    print('Hello world')


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


def load(mapper=lambda v: v):
    data = []
    name = []

    with open('../data/bank.csv') as fp:
        for linage, line in enumerate(fp):
            line = line.strip('\n')
            print(f'{linage} => {line}')
            split = line.split(';')
            for idx, item in enumerate(split):
                split[idx] = item.strip('"')
            if linage == 0:
                name = split
                continue
            data.append(mapper(split))
    return data, name


def bank_mapper(line):
    rtn = [line[k] for k in range(8)]
    item = int(line[0])
    if item < 30:
        rtn[0] = "below"
    elif item < 40:
        rtn[0] = "30s"
    elif item < 50:
        rtn[0] = "40s"
    else:
        rtn[0] = "above"

    item = int(line[5])
    if item < 0:
        rtn[5] = "minus"
    elif item < 1000:
        rtn[5] = "low"
    else:
        rtn[5] = "high"
    return rtn


def divide_data(orig_data, test_size):
    random.Random(17).shuffle(orig_data)
    return orig_data[:test_size], orig_data[test_size:]


def exam(test_data, think_method):
    def judge(v):
        return v == 'yes'

    statics = {'passP': 0, 'failP': 0, 'passN': 0, 'failN': 0}
    for item in test_data:
        result = think_method(item)
        if judge(result):
            if judge(item[-1]):
                desc = 'passP'
            else:
                desc = 'failP'
        else:
            if judge(item[-1]):
                desc = 'failN'
            else:
                desc = 'passN'
        statics[desc] += 1
    print(statics)
