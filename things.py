from random import randint


class Thing:
    BRIEF_DESC_THING_CLASS = 'thing'

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_attack = randint(*self.RANGE_VALUE_ATTACK)
        return value_attack

    def defence(self):
        value_defence = randint(*self.RANGE_VALUE_DEFENCE)
        return value_defence
    
    def healing(self):
        value_healing = randint(*self.RANGE_VALUE_HEALING)
        return value_healing

    # def __str__(self):
    #     return f'{self.__class__.__name__} - {self.BRIEF_DESC_THING_CLASS}.'

class MagicRing(Thing):
    BRIEF_DESC_THING_CLASS = ('магическое кольцо')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    RANGE_VALUE_HEALING = (0, 0)


class Sword(Thing):
    BRIEF_DESC_THING_CLASS = ('меч')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (0, 0)
    RANGE_VALUE_HEALING = (0, 0)


class Shield(Thing):
    BRIEF_DESC_THING_CLASS = ('щит')
    RANGE_VALUE_ATTACK = (0, 0)
    RANGE_VALUE_DEFENCE = (2, 8)
    RANGE_VALUE_HEALING = (0, 0)

class Bow(Thing):
    BRIEF_DESC_THING_CLASS = ('лук')
    RANGE_VALUE_ATTACK = (2, 5)
    RANGE_VALUE_DEFENCE = (0, 0)
    RANGE_VALUE_HEALING = (0, 0)

class Herbs(Thing):
    BRIEF_DESC_THING_CLASS = ('магичекое зелье')
    RANGE_VALUE_ATTACK = (0, 0)
    RANGE_VALUE_DEFENCE = (0, 0)
    RANGE_VALUE_HEALING = (1, 5)


# def pack():
#     sword_attack = Sword().attack()
#     ring_attack = MagicRing().attack()
#     ring_defence = MagicRing().defence()
#     shield_defence = Shield().defence()
#     bow_attack = Bow().attack()
#     sum_attack = sword_attack+ring_attack+bow_attack
#     sum_defence = ring_defence+shield_defence
#     return  sum_attack, sum_defence

