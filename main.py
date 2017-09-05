from room import Room
from item import Item

kitchen = Room("Kitchen")

kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A grand room with a table")

ballroom = Room("Ballroom")
ballroom.set_description("A large room with room to dance")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")

ballroom.link_room(dining_hall,"east")
dining_hall.link_room(ballroom,"west")

current_room = kitchen          

'''
while True:		
    print("\n")         
    current_room.get_details()         
    command = input("> ")    
    current_room = current_room.move(command)  
'''

dagger = Item("Dagger")
dagger.set_description("A combat knife")
dagger.get_details()



