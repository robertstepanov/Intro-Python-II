# Implement a class to hold room information. This should have name and
# description attributes.


# class Room:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

#     def __str__(self):
#         return f"{self.name}: {self.description}"

from item import Item


class Room:

    treasure = []

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}"

    def print_description(self):
        return f"{self.description}"

    def add_item(self, item: Item):
        self.treasure.append(item)

    def goodies(self, name, description):
        self.name = name
        self.description = description
