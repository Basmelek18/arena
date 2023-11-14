from random import sample, randint

from warriors import Warrior, Palladin

from things_pack import one_pack


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

warriors_quantity  = 10
warrior_number = randint(0, warriors_quantity)
warrior_name_list = sample(list_names, 10)
palladin_name_list = list(set(list_names) - set(warrior_name_list))


def our_characters():
    warrior_list_init = [Warrior(name) for name in sample(
        warrior_name_list, warrior_number)]
    palladin_list_init = [Palladin(name) for name in sample(
        palladin_name_list, warriors_quantity - warrior_number)]
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


def complete_character(chars):
    for char in chars:
        pack = shmot_sum(one_pack())
        char.set_things((pack)[0], (pack)[1], (pack)[2], (pack)[3])
    return char


warrior_list = our_characters()
complete_character(warrior_list)


def battle(fighter_1, fighter_2):
    print('''

            ''')
    print(f'На арену выходят воины: {fighter_1.name} и {fighter_2.name}')
    print(f'Очки здоровья: {fighter_1.name} {fighter_1.health()}    {fighter_2.name} {fighter_2.health()}')
    print(fighter_1.name, 'предметы', fighter_1.nishtyaki)
    print(fighter_2.name, 'предметы', fighter_2.nishtyaki)
    print('+-----------------------------------+')

    while fighter_1.health() > 0 and fighter_2.health() > 0:
        fighter_1_attack = fighter_1.attack()
        fighter_2_attack = fighter_2.attack()
        fighter_1.taken_damage(fighter_2_attack)
        print(f'{fighter_2.name} бьет {fighter_1.name} и наносит урон {fighter_2_attack}')
        print(f'Очки здоровья: {fighter_1.name} {fighter_1.health()}    {fighter_2.name} {fighter_2.health()}')
        print('+-----------------------------------+')
        if fighter_1.health() <= 0:
            warrior_list.remove(fighter_1)
            print('')
            print(f'{fighter_2.name} THE WINNER!')
            print('')
            break

        fighter_2.taken_damage(fighter_1_attack)
        print(f'{fighter_1.name} бьет {fighter_2.name} и наносит урон {fighter_1_attack}')
        print(f'Очки здоровья: {fighter_1.name} {fighter_1.health()}    {fighter_2.name} {fighter_2.health()}')
        print('+-----------------------------------+')
        if fighter_2.health() <= 0:
            warrior_list.remove(fighter_2)
            print('')
            print(f'{fighter_1.name} THE WINNER!')
            print('')
            break
    if len(warrior_list) > 1:
        print(f'Воинов осталось: {len(warrior_list)}')


while len(warrior_list) > 1:
    warrior_num = randint(2, warriors_quantity)  
    battle(warrior_list[0], warrior_list[warrior_num - 1])
    warriors_quantity -= 1
