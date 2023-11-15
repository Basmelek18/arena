from random import sample, randint
from time import sleep

from warriors import Warrior, Palladin

from things_pack import one_pack


WARRIORS_QUANTITY = 10
ITEMS_QUANTITY = 4
PACKS_OF_ITEMS_QUANTITY = 50

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

warrior_number = randint(0, WARRIORS_QUANTITY)
warrior_name_list = sample(list_names, int(len(list_names) / 2))
palladin_name_list = list(set(list_names) - set(warrior_name_list))


def our_characters():
    warrior_list_init = [Warrior(name) for name in sample(
        warrior_name_list, warrior_number)]
    palladin_list_init = [Palladin(name) for name in sample(
        palladin_name_list, WARRIORS_QUANTITY - warrior_number)]
    return warrior_list_init + palladin_list_init


def shmot_sum(dict_things):
    thing_name = []
    sum_attack = 0
    sum_defence = 0
    sum_hp = 0
    for name, el in dict_things.items():
        sum_attack += el[0]
        sum_defence += el[1]
        sum_hp += el[2]
        thing_name.append(name)
    return [sum_attack, sum_defence, sum_hp, thing_name]


def create_few_packs_of_items(all_number=20):
    all_packs = []
    for one_num in range(all_number):
        all_packs.append(shmot_sum(one_pack(ITEMS_QUANTITY)))
    return all_packs


def complete_character(chars):
    for char in chars:
        pack = create_few_packs_of_items(
            PACKS_OF_ITEMS_QUANTITY
        )[randint(0, PACKS_OF_ITEMS_QUANTITY - 1)]
        char.set_things(pack[0], pack[1], pack[2], pack[3])
    return char


warrior_list = our_characters()
complete_character(warrior_list)


def battle(fighter_1, fighter_2):
    print('''

            ''')
    print(
        f'На арену выходят воины: '
        f'{fighter_1.__class__.__name__} {fighter_1.name} и '
        f'{fighter_2.__class__.__name__} {fighter_2.name}'
    )
    print(
        f'Очки здоровья: '
        f'{fighter_1.name} {fighter_1.health()}    '
        f'{fighter_2.name} {fighter_2.health()}'
    )
    print(fighter_1.name, 'предметы', fighter_1.nishtyaki)
    print(fighter_2.name, 'предметы', fighter_2.nishtyaki)
    print('+-----------------------------------+')
    # sleep(1)
    while fighter_1.health() > 0 and fighter_2.health() > 0:
        fighter_1_attack = fighter_1.attack()
        fighter_2_attack = fighter_2.attack()
        fighter_1.taken_damage(fighter_2_attack)
        print(
            f'{fighter_2.name} бьет {fighter_1.name} '
            f'и наносит урон {fighter_2_attack}'
        )
        print(
            f'Очки здоровья: {fighter_1.name} {fighter_1.health()}    '
            f'{fighter_2.name} {fighter_2.health()}'
        )
        print('+-----------------------------------+')
        if fighter_1.health() <= 0:
            warrior_list.remove(fighter_1)
            print('')
            print(
                f'{fighter_2.__class__.__name__} '
                f'{fighter_2.name} THE WINNER!'
            )
            print('')
            break
        # sleep(1)
        fighter_2.taken_damage(fighter_1_attack)
        print(
            f'{fighter_1.name} бьет {fighter_2.name} '
            f'и наносит урон {fighter_1_attack}'
        )
        print(
            f'Очки здоровья: {fighter_1.name} {fighter_1.health()}    '
            f'{fighter_2.name} {fighter_2.health()}'
        )
        print('+-----------------------------------+')
        if fighter_2.health() <= 0:
            warrior_list.remove(fighter_2)
            print('')
            print(
                f'{fighter_1.__class__.__name__} '
                f'{fighter_1.name} THE WINNER!'
            )
            print('')
            break
    if len(warrior_list) > 1:
        print(f'Воинов осталось: {len(warrior_list)}')


while len(warrior_list) > 1:
    warrior_num = randint(2, WARRIORS_QUANTITY)  
    battle(warrior_list[0], warrior_list[warrior_num - 1])
    WARRIORS_QUANTITY -= 1
