from things_pack import the_things


def shmot_sum(dict_things):
    thing_name = []
    sum_attack = 0
    sum_defence = 0
    sum_hp = 0
    for name, el in dict_things.items():
        thing_name.append(name)
        sum_attack += el[0]
        sum_defence += el[1]
        sum_hp += el[2]
    return [sum_attack, sum_defence, sum_hp, thing_name]
