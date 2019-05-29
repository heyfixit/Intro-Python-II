# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    inventory = []
    def __init__(self, name, room):
        self.current_room = room
        self.name = name

    def __str__(self):
        return f"{self.name}"
