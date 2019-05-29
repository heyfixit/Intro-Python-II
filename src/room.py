# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    n_to = None
    e_to = None
    s_to = None
    w_to = None
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        if(items is None):
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"{self.name} - {self.description}"
