# Creates a random name for a character
import random
import csv

fNames = []
mNames = []
lastNames = []
suffixes = []
prefixes = []
with open("data/namesList.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for lines in csv_reader:
        lastNames.append(lines[0])
        fNames.append(lines[1])
        mNames.append(lines[2])
        suffixes.append(lines[3])
        prefixes.append(lines[4])

    
def generateName(gender):
    if(gender == 0):
        #generate female name
        fName = ''
        lastName = ''
        while fName == '':
            fName = (str(fNames[random.randint(0,(len(fNames) - 1))]))
        while lastName == '':
            lastName = (str(lastNames[random.randint(0, (len(lastNames) - 1))]))
        return str(fName + " " + lastName)
    else: 
        #generate male name
        mName = ''
        lastName = ''
        while mName == '':
            mName = (str(mNames[random.randint(0,(len(mNames) - 1))]))
        while lastName == '':
            lastName = (str(lastNames[random.randint(0, (len(lastNames) - 1))]))
        return str(mName + " " +lastName)
