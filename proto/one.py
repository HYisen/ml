from proto.util import *

data, _ = load()

# scan(data, 0, 10)
# print('age|balance')
# scan(data, 5, 1000)

good, _ = load(bank_mapper)

# show(good, 10)

test, train = divide_data(good, 1000)

stat = (collections.defaultdict(int), collections.defaultdict(int))


def knn(item):
    neighbours = []
    min_dist = len(item)
    for one in train:
        new_dist = len(item) - 1
        for idx, two in enumerate(one):
            if idx == len(one) - 1:
                continue
            if two == item[idx]:
                new_dist -= 1
            if new_dist <= min_dist:
                if new_dist < min_dist:
                    min_dist = new_dist
                    neighbours.clear()
                neighbours.append(one)
    count = 0
    for neighbour in neighbours:
        if neighbour[-1] == 'yes':
            count += 1
    rate = count / len(neighbours)

    # print(f'dist {min_dist} with {len(neighbours)} posRate={rate:5.3f}')
    stat[0][min_dist] += 1
    stat[1][int(len(neighbours) / 10)] += 1

    return 'yes' if rate > 0.5 else 'no'


exam(test, knn)

print(stat[0])
print(sorted(stat[1].items()))
