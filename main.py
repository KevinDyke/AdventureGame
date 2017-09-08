from room import Room
from item import Item
from character import Enemy
from character import Friend

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
banker = Friend("Banker","A Friendy Bank Manager - Well this is a fanasty!!!!")        
banker.set_conversation("Its going to cosh you!!")
banker.set_cash(500)
kitchen.set_character(banker)

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

mark = Enemy("Mark","A greedy Goblin")
mark.set_conversation("Give me all your money")
mark.set_weakness("cheese")
mark.set_bribe(50)
ballroom.set_character(mark)

dagger = Item("Dagger")
dagger.set_description("A combat knife")
dagger.get_details()

while True:		
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
         
    command = input("> ")    
    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            combat_item = input("What are you gonna fight with!")
            survive = inhabitant.fight(combat_item)
            if survive:
                print("You live to fight another day")
            else:
                print("Game over!")
                break
    elif command == "bribe":
        if inhabitant is not None:
            cash = int(input("How are going to bribe with!"))
            survive = inhabitant.bribe(cash)
            if survive:
                print("You live to fight another day")
            else:
                print("Game over!")
                break
    elif command == "borrow":
        if inhabitant is not None:
            cash = inhabitant.borrow_money()
            
    
    


