import random
import csv

occupations = []
trained_weapons = []
trade_goods = []
farmer_type = []
with open("data/occupationTable.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        occupations.append(lines[0])
        trained_weapons.append(lines[1])
        trade_goods.append(lines[2])
with open("data/farmerTypeTable.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
    for lines in csv_reader:
        farmer_type.append(lines[0]

def generate_farmer():
    farmer = farmer_type[random.randint(0, (len(farmer_type) - 1))]
    return str(farmer)

def generate_occupation():
    roll = random.randint(0,100)
    if roll == range(38, 47):
        generate_farmer()

    occupation_stuff = occupation + ', ' + trained_weapon + ', ' + trade_goods)

    return str(occupation_stuff)
