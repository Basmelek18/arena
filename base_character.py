from random import randint


class BaseCharacter:

    def __init__(self, name, attack=100, defence=0, hp=100, nishtyaki=''):
        self.name = name
        self.start_attack = attack
        self.start_defence = defence
        self.start_hp = hp

    def attack(self):
        start_attack = randint(30, self.start_attack)
        return start_attack

    def defence(self):
        return self.start_defence

    def health(self):
        return self.start_hp

    def taken_damage(self, attack_damage):
        after_armor = self.start_defence - attack_damage
        if after_armor <= 0:
            self.start_defence = 0
            self.start_hp = self.start_hp + after_armor
        else:
            self.start_defence = after_armor
        return after_armor
