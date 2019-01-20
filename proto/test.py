from proto.util import *

orig, name = load(bank_mapper)

test, train = divide_data(orig, 1000)


def all_yes(data):
    return 'yes'


exam(test, all_yes)
