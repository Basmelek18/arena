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
    for thing in sample(things_list, randint(0, 4)):
        return thing
        # print(f'    {thing.name} attack', thing.attack())
        # print(f'    {thing.name} defence', thing.defence())
        # print(f'    {thing.name} healing', thing.healing())
        # print(' ')

    

# the_things()
