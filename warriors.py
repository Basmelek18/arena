from base_character import BaseCharacter


class Warrior(BaseCharacter):

    def set_things(self, extra_attack=0, extra_def=0, extra_hp=0, nishtyaki=''):
            self.start_attack = extra_attack + self.attack() * 2
            self.start_defence = extra_def + self.defence()
            self.start_hp = extra_hp + self.health()
            self.nishtyaki = nishtyaki


class Palladin(BaseCharacter):

    def set_things(self, extra_attack=0, extra_def=0, extra_hp=0, nishtyaki=''):
            self.start_attack = extra_attack + self.attack()
            self.start_defence = extra_def + self.defence() * 2
            self.start_hp = extra_hp + self.health() * 2
            self.nishtyaki = nishtyaki
