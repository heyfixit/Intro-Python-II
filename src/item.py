class Item:
    def __init__(self, name, description):
        self.description = description
        self.name = name

    def __str__(self):
        return f"{self.name} - {self.description}"
