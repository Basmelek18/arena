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

    def set_things(self, *args):
        return {
            'sum_damage': args[0] + DEFAULT_ATTACK,
            'sum_defence': args[1] + DEFAULT_DEFENCE,
            'sum_hp': args[2] + DEFAULT_HP
        }


teo = BaseCharacter('oleg').set_things(2, 20, 10)
print(teo)

