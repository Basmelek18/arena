DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_HP = 100


class BaseCharacter:

    def __init__(self, name):
        self.name = name

    def attack(self):
        return self.set_things['sum_damage']

    def defence(self):
        return self.set_things['sum_defence']

    def hells(self):
        return self.set_things['sum_hp']

    def set_things(self, extra_attack, extra_def, extra_hp):
        return {
            'sum_damage': extra_attack + DEFAULT_ATTACK,
            'sum_defence': extra_def + DEFAULT_DEFENCE,
            'sum_hp': extra_hp + DEFAULT_HP
        }
