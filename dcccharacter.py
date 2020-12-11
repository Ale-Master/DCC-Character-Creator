import random
import nameGen
import csv
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
    print(str(name))
    print(strength)
    print(agility)
    print(stamina)
    print(personality)
    print(intelligence)
    print(luck)
else:
    save = input("Would you like to save your character(s)? (y/n)")
    if save == ("y"):
        print("Saving...")
        f= open('Character.csv','w+')
        f.write(name+ '\n')
        f.write(strength +'\n')
        f.write(agility +'\n')
        f.write(stamina +'\n')
        f.write(personality +'\n')
        f.write(intelligence +'\n')
        f.write(luck +'\n')
        f.close()
        print("Saved!")
        print("Goodbye.")
#add a way to save a character to a .csv
    else:
        print("Goodbye.")