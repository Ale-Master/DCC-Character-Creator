import random
import nameGen
import csv
number = int(input("How many characters would you like to create?"))
#d6 = random.randint(1,6)
with open('characterlist.csv', mode='w') as csv_file:
    fieldnames = ['character files',]
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
    #modifier calculation could be shrunk I'm sure...
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
    
    #end of modifier calculation
    print(str(name))
    print(strength)
    print(agility)
    print(stamina)
    print(personality)
    print(intelligence)
    print(luck)
    with open(name + '.csv', mode='w') as csv_file:
        fieldnames = ['stat_name', 'stat_value', 'stat_mod',]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'stat_name': 'strength', 'stat_value': stat1, 'stat_mod': strmod, })
        writer.writerow({'stat_name': 'agility', 'stat_value': stat2, 'stat_mod': agimod })
        writer.writerow({'stat_name': 'stamina', 'stat_value': stat3, })
        writer.writerow({'stat_name': 'personality', 'stat_value': stat4, })
        writer.writerow({'stat_name': 'intelligence', 'stat_value': stat5, })
        writer.writerow({'stat_name': 'luck', 'stat_value': stat6, })
    with open('characterlist.csv', 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow([name + '.csv'])
else:
    save = input("Would you like to save your character(s)? (y/n)")
    if save == ("y"):
        print("Saving...")
        print("Saved!")
        print("Goodbye.")
#add a way to save a character to a .csv
    else:
        print("Goodbye.")