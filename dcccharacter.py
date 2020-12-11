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
    print("Str = " + str(strength))
    print("Agi = " + str(agility))
    print("Sta = " + str(stamina))
    print("Per = " + str(personality))
    print("Int = " + str(intelligence))
    print("Luc = " + str(luck))
else:
    save = input("Would you like to save your character(s)? (y/n)")
    if save == ("y"):
        print("Saving...")
        print("Goodbye.")
#add a way to save a character to a .csv
    else:
        print("Goodbye.")