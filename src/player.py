# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items=None):
        self.current_room = room
        self.name = name
        if(items is None):
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"{self.name}"

    def add_item(self, item):
        self.items.append(item)
        self.on_take(item)

    def drop_item(self, item):
        self.items.remove(item)
        self.on_drop(item)

    def on_take(self, item):
        print(f"You have picked up {item.name}.")

    def on_drop(self, item):
        print(f"You have dropped {item.name}.")
