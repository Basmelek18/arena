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

    def health(self):
        value_healing = randint(*self.RANGE_VALUE_HEALING)
        return value_healing


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
