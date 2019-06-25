# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.name = name
        self.description = description
        if(items is None):
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"{self.name} - {self.description}"

    def remove_item(self, name):
        # one liner to find the first matching item or None
        found_item = next((item for item in self.items if item.name == name), None)
        if found_item is not None:
            self.items.remove(found_item)
            return found_item
        else:
            return False

    def available_directions(self):
        return [d for d in ['w', 'e', 's', 'n'] if getattr(self, f"{d}_to") is not None]
