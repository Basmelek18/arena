class BaseCharacter:

    def __init__(self, name, attack=5, defence=0, hp=100):
        self.name = name
        self.start_attack = attack
        self.start_defence = defence
        self.start_hp = hp

    def attack(self):
        return self.start_attack

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
