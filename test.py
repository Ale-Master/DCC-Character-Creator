import random, csv, os
import nameGen

class Character:
    def __init__(self, name, stats, occupation, inventory):
        self.name = name
        self.stats = stats
        self.occupation = occupation
        self.inventory = inventory

    def roll(self, number, faces):
        self.number = number
        self.faces = faces
        result = 0
        for x in range (0, number):
            result = result + random.randint(1, faces)
        return result
    
    def generate(self):
        def getname():
            roll.Name

class Tables(Character):
    def __init__(self, name, file):
        self.name = name
        self.file = file

class Stats(Character):
    def __init__(self, strength, agility, stamina, personality, intelligence, luck):
        self.strength = strength
        self.agility = agility
        self.stamina = 
    def get_stats(self):
        self.roll