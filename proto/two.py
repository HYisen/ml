import collections
from math import log2

from proto.util import *

orig, name = load(bank_mapper)
test, train = divide_data(orig, 1000)


def divide(data, attr_idx):
    rtn = collections.defaultdict(list)
    # print(f'{attr_idx}')
    for line in data:
        rtn[line[attr_idx]].append(line)
    return rtn


def safe_calc(p):
    return 0 if p == 0 else p * log2(p)


def calc_entropy(data):
    pos = [line[-1] for line in data].count('yes') / len(data)
    neg = 1 - pos
    return safe_calc(pos) + safe_calc(neg)


def calc(divided):
    rtn = 0
    for _, value in divided.items():
        rtn += calc_entropy(value) * len(value)
    return rtn


def build_tree(data, possible_index=None):
    if possible_index is None:
        possible_index = [i for i in range(len(data[0]) - 1)]
    count = [line[-1] for line in data].count('yes')
    if count == len(data) or count == 0 or not possible_index:
        return -1, data, count / len(data)
    record = -1e9  # a number so small that every possible one would larger than it.
    index = -1
    best_divided = {}
    for i in possible_index:
        candidate = divide(data, i)
        delta = calc(candidate)
        # print(f'{name[i]}\t{delta}')
        if delta > record:
            record = delta
            best_divided = candidate
            index = i
    possible_index.remove(index)
    for key in best_divided:
        temp = best_divided[key]
        best_divided[key] = build_tree(temp, possible_index.copy())
    return index, best_divided, count / len(data)


def print_tree(depth, node, attr):
    prefix = ' ' * (depth * 4)
    index = node[0]
    if index == -1:
        print(f'{prefix}{attr} LEAF {node[2]:5.3f} of {len(node[1])}')
        return
    else:
        print(f'{prefix}{attr}->{index}:{name[index]:10s}{node[2]:5.3f} of {len(node[1])}')
        for attr, leaf in node[1].items():
            print_tree(depth + 1, leaf, attr)


tree = build_tree(train)

print_tree(0, tree, 'root')


def dt(data):
    node = tree
    while node[0] != -1:
        next_node = node[1][data[node[0]]]
        if not next_node:
            break
        node = next_node
    rate = node[2]
    print(f'{rate:5.3f} of {len(node[1])}')
    return 'yes' if rate > 0.5 else 'no'


exam(test, dt)
