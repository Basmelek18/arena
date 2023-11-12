class BaseCharacter:

    def __init__(self, name, attack=5, defence=10, hp=100):
        self.name = name
        self.start_attack = attack
        self.start_defence = defence
        self.start_hp = hp

    def attack(self):
        return self.start_attack

    def defence(self):
        return self.start_defence

    def hells(self):
        return self.start_hp

    def set_things(self, extra_attack=0, extra_def=0, extra_hp=0):
            self.start_attack = extra_attack + self.attack()
            self.start_defence = extra_def + self.defence()
            self.start_hp = extra_hp + self.hells()


#    def taken_damage(self, attack_damage):
#        after_armor = self.set_things()['extra_defence'] - attack_damage
#        self.start_hp = self.set_things()['extra_hp'] + after_armor
 #       if after_armor >= 0:
 #           self.start_defence = 0
  #      self.start_defence =
#