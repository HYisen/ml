from proto.util import *

echo()

good, _ = load(lambda v: v[-1])

cnt = 0

for one in good:
    if one == 'yes':
        cnt += 1

print(cnt)
print(len(good))

print(cnt / len(good))