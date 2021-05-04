import random, csv, os
import nameGen

class Character:
    def __init__(self, name, stats, occupation, inventory):
        self.name = name
        self.stats = stats
        self.occupation = occupation
        self.inventory = inventory

class Dice:
    def __init__(self, number, faces):
        self.number = number
        self.faces = faces
    def roll(self):
        random.randint(1, self.faces)
        return

class Stats:
    def __init__(self):
    def get_stats(self):
        self.roll