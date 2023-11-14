from random import sample, randint

from things import *


THINGS_LIST = []

def all_things():
    for num in range(1, 10):
        THINGS_LIST.append(MagicRing(num))
        THINGS_LIST.append(Sword(num))
        THINGS_LIST.append(Shield(num))
        THINGS_LIST.append(Bow(num))
        THINGS_LIST.append(Herbs(num))
    all_things = sample(THINGS_LIST, randint(0, 4))
    return all_things


def one_pack(range_things=all_things()):
    range_things = sample(THINGS_LIST, randint(0, 4))
    one_pack = {}
    for thing in range_things:
        things = {thing.name: [thing.attack(), thing.defence(), thing.health()]}
        one_pack.update(things)
    return one_pack
