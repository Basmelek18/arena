from random import sample, randint

from things import MagicRing, Sword, Shield, Bow, Herbs

def the_things():
    things_list = [
        MagicRing('ring'),
        Sword('sword'),
        Shield('shield'),
        Bow('bow'),
        Herbs('herb')
    ]
    things_pack = []
    for thing in sample(things_list, randint(0, 4)):
        things = [thing.name, thing.attack(), thing.defence(), thing.healing()]
        things_pack.append(things)

    return things_pack

