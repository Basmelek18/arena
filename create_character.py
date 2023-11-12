import random

from warriors import Warrior, Palladin

from things_pack import the_things
from shmot_sum import shmot_sum


list_names = [
    'Геральт',
    'Йеннифер',
    'Трисс',
    'Цири',
    'Лютик',
    'Вильгот',
    'Эмиль Регис Роггевизен',
    'Зольтан Хиви',
    'Ярпен Зигрин',
    'Весемир',
    'Фольтест',
    'Эйст Тишина',
    'Эмиля Региссон',
    'Милва',
    'Ангуулема',
    'Венсеремарайме',
    'Райнфарн',
    'Ламберт',
    'Эскал',
    'Фрингильа Виго',
]

warrior_num = random.randint(0, 10)
character_name_list = random.sample(list_names, 10)


def our_characters():
    warrior_list = [Warrior(name) for name in random.sample(
        character_name_list, warrior_num)]
    palladin_list = [Palladin(name) for name in random.sample(
        character_name_list, 10 - warrior_num)]
    return warrior_list + palladin_list


def shmot_packs():
    ten_packs = []
    for nomer in range(10):
        packs = the_things()
        # shmot_sum(packs)
        ten_packs.append(shmot_sum(packs))
        print(ten_packs)
    return ten_packs



def complete_character(chars):
    for char in chars:
        th = the_things()
        char.set_things(shmot_sum(th)[0], shmot_sum(th)[1], shmot_sum(th)[2])
    return shmot_sum(th)[3]


warrior_list = our_characters()
complete_character(warrior_list)


def battle(fighter_1, fighter_2):
    while fighter_1.health() > 0 and fighter_2.health() > 0:
        fighter_1_attack = fighter_1.attack()
        fighter_2_attack = fighter_2.attack()
        fighter_1.taken_damage(fighter_2_attack)
        fighter_2.taken_damage(fighter_1_attack)
    if fighter_1.health() <= 0:
        warrior_list.remove(fighter_1)
    elif fighter_2.health() <= 0:
        warrior_list.remove(fighter_2)

quantity = 10

while len(warrior_list) > 1:
    warrior_num = random.randint(1, quantity)  
    battle(warrior_list[0], warrior_list[warrior_num-1])
    # battle(warrior_list[w])
    quantity -= 1
    print(warrior_list)
    print(len(warrior_list))

print(warrior_list[0].name, complete_character([warrior_list[0]]))
