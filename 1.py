from things_pack import the_things

dict_things = the_things()

sum_attack = 0
sum_defence = 0
sum_hp = 0

for name, el in dict_things.items():
    thing_name = name
    extra_attack = el[0]
    extra_defence = el[1]
    extra_hp = el[2]
    sum_attack += extra_attack
    sum_defence += extra_defence
    sum_hp += extra_hp

    
    print(thing_name, extra_attack, extra_defence, extra_hp)
print(sum_attack, sum_defence, sum_hp)