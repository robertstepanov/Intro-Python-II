# Write a class to hold player information, e.g. what room they are in
# currently.


# class Player:
#     def __init__(self, name, current_room, items=[]):
#         self.name = name
#         self.current_room = current_room
#         self.items = items

#     def __str__(self):
#         return f"{self.name} are now in the {self.current_room}"


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def move_to(self, direction, current_loc):
       
        attribute = direction + '_to'
        
        if hasattr(current_loc, attribute):
            
            return getattr(current_loc, attribute)
        
        
        print("You can't go that way\n")
        return current_loc


