from random import randint


class Thing:
    BRIEF_DESC_THING_CLASS = 'thing'

    def __init__(self, num, attack=0, defence=0, hp=0):
        self.name = "_".join([self.BRIEF_DESC_THING_CLASS, str(num)])
        self.start_attack = attack
        self.start_defence = defence
        self.start_hp = hp

    def attack(self):
        attack = randint(*self.RANGE_VALUE_ATTACK)
        return attack

    def defence(self):
        defence = randint(*self.RANGE_VALUE_DEFENCE)
        return defence

    def health(self):
        hp = randint(*self.RANGE_VALUE_HEALING)
        return hp


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
    BRIEF_DESC_THING_CLASS = ('магическое зелье')
    RANGE_VALUE_ATTACK = (0, 0)
    RANGE_VALUE_DEFENCE = (0, 0)
    RANGE_VALUE_HEALING = (1, 5)
