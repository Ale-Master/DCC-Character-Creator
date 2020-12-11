import random
import nameGen
import csv
import os
#d6 = random.randint(1,6)
print("Welcome to DCC Level 0 Character Generator! \n")

def startMenu():
    charsListLoc = 'characterExports'
    charListFiles = []
    for r, d, f in os.walk(charsListLoc):
        for item in f:
            if '.csv' in item:
                charListFiles.append(item)
    print("You have " + str(len(charListFiles)) + " character lists. \n")
    print("[C] - Create New Character List \n")
    print("[A] - Add to Previous Character List \n")
    response = input("[Q] - Quit \n")
    response = response.lower()

    if(response == "c"):
        newFilename = input("Please name your new character list.")
        newFilename = "characterExports/" + newFilename.replace('.csv','') + ".csv"
        f = open(newFilename,'w+')
        f.write("Name,")
        f.write("Strength,")
        f.write("Agility,")
        f.write("Stamina,")
        f.write("Personality,")
        f.write("Intelligence,")
        f.write("Luck" + '\n')
        genCharacter(f)
        print("Characters exported to " + newFilename)
    elif (response == 'a'):
        print("Your recent character lists:")
        for item in charListFiles:
            print(str(item))
        prevFilename = input("Enter the name of the file you wish to edit")       
        prevFilename = "characterExports/" + prevFilename.replace('.csv','') + ".csv"
        f = open(prevFilename,'a+')
        genCharacter(f)
        print("Characters exported to " + prevFilename)
    else:
        return

    f.close()
    print("Goodbye.")


def genCharacter(f):
    number = int(input("How many characters would you like to create?"))    
    for x in range(number):
        # TODO: Put in actual character generator
        # Generate character stats
        stat1 = ((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
        stat2 = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
        stat3 = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
        stat4 = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
        stat5 = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
        stat6 = int((random.randint(1,6)) + (random.randint(1,6)) + (random.randint(1,6)))
        strength = (str(stat1))
        agility = (str(stat2))
        stamina = (str(stat3))
        personality = (str(stat4))
        intelligence = (str(stat5))
        luck = (str(stat6))
        gender = int((random.randint(0,1)))
        name = nameGen.generateName(gender)
        # Display character stats
        print(str(name))
        print(str("Str = " + strength))
        print(str("Agi = " + agility))
        print(str("Sta = " + stamina))
        print(str("Per = " + personality))
        print(str("Int = " + intelligence))
        print(str("Luc = " + luck))
        # Save character stats to .csv file
        f.write(name + ',')
        f.write(strength +',')
        f.write(agility +',')
        f.write(stamina +',')
        f.write(personality +',')
        f.write(intelligence +',')
        f.write(luck + '\n')

startMenu()