class Room():
    """ describes a room in the adventure games and handles characters and items in the room """
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.character = None
        self.item = None
        self.linked_rooms = {}

    def set_description(self, room_description):
        """ sets the description of the room """
        self.description = room_description

    def get_description(self):
        """ returns the description of the room """
        return self.description

    def get_name(self):
        """ returns the name of the room """
        return self.name

    def set_name(self, name):
        """ sets the name of the room """
        self.name = name

    def describe(self):
        """ prints out a copy of the room's description """
        print( self.description )

    def link_room(self, room_to_link, direction):
        """ holds a list of the other rooms the room is linked to """
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_details(self):
        """ displays a description of the room, who is in it and any item present """
        print(self.name)
        print("-------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)

    def move(self, direction):
        """ check if a move can be made and so move else display error message """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def set_character(self,character):
        """ sets the character being in the room """
        self.character = character
        
    def get_character(self):
        """ gets the character's name for this room """
        return self.character

    def get_item(self):
        """ gets the item in this room """
        return self.item

    def set_item(self,item):
        """ set the item being in this rooom """
        self.item = item
        
