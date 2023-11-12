from base_character import BaseCharacter


class Warrior(BaseCharacter):

    def attack(self):
        return self.start_attack * 2


class Palladin(BaseCharacter):

    def defence(self):
        return self.start_defence * 2

    def hells(self):
        return self.start_hp * 2


test_w = Warrior('fedya', 2, 3, 4).set_things(10, 20, 40)
print(test_w)