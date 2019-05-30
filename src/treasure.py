from item import Item
from termcolor import colored

class Treasure(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def __str__(self):
        return colored(f"{self.name} - {self.description}", 'green')
