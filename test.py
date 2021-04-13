import random
import nameGen
import csv
import os

num = int(input('How many characters would you like to generate?'))
stats = ['strength', 'agility', 'stamina', 'personality', 'intelligence', 'luck']
character_list = ['']
stat_list = ['']
mod_list = ['']
for x in range(num):
    gender = random.randint(0, 1)
    name = nameGen.generateName(gender)
    stat_list = ['']
    mod_list = ['']
    y = 1
    print(name)
    with open('data/newCharacters/' + name + '.csv', mode='w', newline='') as csv_file:
        fieldnames = ['stat_name', 'stat_value', 'stat_mod', ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

    for e in stats:
        stat = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6))
        mod = round(
            -5.667044 + 1.164034 * stat - 0.0891879 * stat ** 2 + 0.002831362 * stat ** 3 - 3.7775049999999997e-19 * stat ** 4)
        stat_list.append(str(stat))
        mod_list.append(str(mod))
        with open('data/newCharacters/' + name + '.csv', mode='a', newline='') as csv_file:
            fieldnames = ['stat_name', 'stat_value', 'stat_mod', ]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow({'stat_name': e, 'stat_value': stat_list[y], 'stat_mod': mod_list[y]})
            y = y + 1
        print(e + ' Score:' + str(stat) + ' Mod:' + str(mod))
    with open('data/newCharacters/characterlist.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow({name + '.csv'})