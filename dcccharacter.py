import random
import csv
number = int(input("How many characters would you like to create?"))
#d6 = random.randint(1,6)
for x in range(number):
    #put in actual character generator
    strength = ((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    agility = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    stamina = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    personality = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    intelligence = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    luck = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
    stat1 = ("Str = " + str(strength))
    stat2 = ("Agi = " + str(agility))
    stat3 = ("Sta = " + str(stamina))
    stat4 = ("Per = " + str(personality))
    stat5 = ("Int = " + str(intelligence))
    stat6 = ("Luc = " + str(luck))
    print(stat1)
    print(stat2)
    print(stat3)
    print(stat4)
    print(stat5)
    print(stat6)
else:
    save = input("Would you like to save your character(s)? (y/n)")
    if save == ("y"):
        print("Saving...")
        print("Saved!")
        print("Goodbye.")
#add a way to save a character to a .csv
    else:
        print("Goodbye.")