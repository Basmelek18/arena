from random import sample, randint

from things import *

THINGS_LIST = [
        MagicRing('ring'),
        Sword('sword'),
        Shield('shield'),
        Bow('bow'),
        Herbs('herb')
    ]
RANGE_THINGS = sample(THINGS_LIST, randint(0, 4))

def the_things(range_things=RANGE_THINGS):
    things_pack = {}
    for thing in range_things:
        things = {thing.name: [thing.attack(), thing.defence(), thing.health()]}
        things_pack.update(things)
    return things_pack
