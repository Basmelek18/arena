import random

from warriors import Warrior, Palladin


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

warrior_list = [Warrior(name) for name in random.sample(
    character_name_list, warrior_num)]

palladin_list = [Palladin(name) for name in random.sample(
    character_name_list, 10 - warrior_num)]

print(warrior_list, palladin_list)
for character in warrior_list:
    print(character.set_things())
for character in palladin_list:
    print(character.set_things())
