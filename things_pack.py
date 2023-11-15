from random import sample, randint

from things import *


NUMBER_OF_VARIETY_OF_ITEMS = 20

def create_things():
    things_list = []
    for num in range(NUMBER_OF_VARIETY_OF_ITEMS):
        things_list.append(MagicRing(num))
        things_list.append(Sword(num))
        things_list.append(Shield(num))
        things_list.append(Bow(num))
        things_list.append(Herbs(num))
    return things_list


def one_pack(number_of_items_in_pack=4):
    range_things = sample(create_things(), randint(0, number_of_items_in_pack))
    one_pack = {}
    for thing in range_things:
        things = {thing.name: [thing.attack(), thing.defence(), thing.health()]}
        one_pack.update(things)
    return one_pack
