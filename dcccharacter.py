import random
import nameGen
import csv
import os
number = int(input("How many characters would you like to create?"))
#d6 = random.randint(1,6)
for x in range(number):
    #put in actual character generator
    stat1 = ((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    stat2 = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    stat3 = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    stat4 = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    stat5 = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    stat6 = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    strength = ("Str = " + str(stat1))
    agility = ("Agi = " + str(stat2))
    stamina = ("Sta = " + str(stat3))
    personality = ("Per = " + str(stat4))
    intelligence = ("Int = " + str(stat5))
    luck = ("Luc = " + str(stat6))
    gender = int((random.randint(0,1)))
    name = nameGen.generateName(gender)
    #strength modifier
    if stat1 == 18:
        strmod = '+3'
    elif stat1 <= 17 and stat1 >= 16:
        strmod = '+2'
    elif stat1 <= 15 and stat1 >= 13:
        strmod = '+1'
    elif stat1 <= 12 and stat1 >= 9:
        strmod = '0'
    elif stat1 <= 8 and stat1 >= 6:
        strmod = '-1'
    elif stat1 <= 5 and stat1 >= 4:
        strmod = '-2'
    elif stat1 == 3:
        strmod = '-3'
    #agility modifier
    if stat2 == 18:
        agimod = '+3'
    elif stat2 <= 17 and stat2 >= 16:
        agimod = '+2'
    elif stat2 <= 15 and stat2 >= 13:
        agimod = '+1'
    elif stat2 <= 12 and stat2 >= 9:
        agimod = '0'
    elif stat2 <= 8 and stat2 >= 6:
        agimod = '-1'
    elif stat2 <= 5 and stat2 >= 4:
        agimod = '-2'
    elif stat2 == 3:
        agimod = '-3'
    #stamina modifier
    if stat3 == 18:
        stamod = '+3'
    elif stat3 <= 17 and stat3 >= 16:
        stamod = '+2'
    elif stat3 <= 15 and stat3 >= 13:
        stamod = '+1'
    elif stat3 <= 12 and stat3 >= 9:
        stamod = '0'
    elif stat3 <= 8 and stat3 >= 6:
        stamod = '-1'
    elif stat3 <= 5 and stat3 >= 4:
        stamod = '-2'
    elif stat3 == 3:
        stamod = '-3'
    #personality modifier
    if stat4 == 18:
        permod = '+3'
    elif stat4 <= 17 and stat4 >= 16:
        permod = '+2'
    elif stat4 <= 15 and stat4 >= 13:
        permod = '+1'
    elif stat4 <= 12 and stat4 >= 9:
        permod = '0'
    elif stat4 <= 8 and stat4 >= 6:
        permod = '-1'
    elif stat4 <= 5 and stat4 >= 4:
        permod = '-2'
    elif stat4 == 3:
        permod = '-3'
    #intelligence modifier
    if stat5 == 18:
        intmod = '+3'
    elif stat5 <= 17 and stat5 >= 16:
        intmod = '+2'
    elif stat5 <= 15 and stat5 >= 13:
        intmod = '+1'
    elif stat5 <= 12 and stat5 >= 9:
        intmod = '0'
    elif stat5 <= 8 and stat5 >= 6:
        intmod = '-1'
    elif stat5 <= 5 and stat5 >= 4:
        intmod = '-2'
    elif stat5 == 3:
        intmod = '-3'
    #luck modifier
    if stat6 == 18:
        lucmod = '+3'
    elif stat6 <= 17 and stat6 >= 16:
        lucmod = '+2'
    elif stat6 <= 15 and stat6 >= 13:
        lucmod = '+1'
    elif stat6 <= 12 and stat6 >= 9:
        lucmod = '0'
    elif stat6 <= 8 and stat6 >= 6:
        lucmod = '-1'
    elif stat6 <= 5 and stat6 >= 4:
        lucmod = '-2'
    elif stat6 == 3:
        lucmod = '-3'
    print(str(name))
    print(strength)
    print(agility)
    print(stamina)
    print(personality)
    print(intelligence)
    print(luck)
    with open('data/newCharacters/' + name + '.csv', mode='w',newline='') as csv_file:
        fieldnames = ['stat_name', 'stat_value', 'stat_mod',]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'stat_name': 'strength', 'stat_value': stat1, 'stat_mod': strmod })
        writer.writerow({'stat_name': 'agility', 'stat_value': stat2, 'stat_mod': agimod })
        writer.writerow({'stat_name': 'stamina', 'stat_value': stat3, 'stat_mod': stamod })
        writer.writerow({'stat_name': 'personality', 'stat_value': stat4, 'stat_mod': permod })
        writer.writerow({'stat_name': 'intelligence', 'stat_value': stat5, 'stat_mod': intmod })
        writer.writerow({'stat_name': 'luck', 'stat_value': stat6, 'stat_mod': lucmod })
    with open('data/newCharacters/characterlist.csv', 'a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow({name + '.csv'})
else:
    while True:
        save = input("Would you like to save your character(s)? (y/n)")
        if save == 'y':
            end = 1
        elif save == 'n':
            end = 1
        else:
            end = 0
        if not end == 1:
            continue
        else:
            break
    if save == ("y"):
        print("Saving...")
        f = open('data/newCharacters/characterlist.csv', 'r')
        for x in range(number):
            character = (f.readline())
            os.rename('data/newCharacters/' + character.rstrip('\n'), 'data/savedCharacters/' + character.rstrip('\n'))
        f.close()
        os.remove ('data/newCharacters/characterlist.csv')
        print("Saved!")
        print("Goodbye.")
#add a way to save a character to a .csv
    elif save == ('n'):
        f = open('data/newCharacters/characterlist.csv', 'r')
        for x in range(number):
            character = (f.readline())
            #path = ('data/newCharacters/' + character)

            os.remove ('data/newCharacters/' + character.rstrip('\n'))
        f.close()
        os.remove ('data/newCharacters/characterlist.csv')
        print("Goodbye.")