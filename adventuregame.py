from room import Room
from item import Item
from character import Enemy, Friend

backpack = []

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
mark.set_weakness("dagger")
mark.set_bribe(50)
ballroom.set_character(mark)

cheese = Item("cheese")
cheese.set_description("A beautiful Somerset Brie!!!")
kitchen.set_item(cheese)

dead = False
while not dead:		
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    item_present = current_room.get_item()
    if item_present is not None:
        print("The following item is present: " + item_present.get_name())
        item_present.get_details()
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
            #
            if combat_item in backpack:
                survive = inhabitant.fight(combat_item)
                if survive:
                    if inhabitant.enemies_defeated == 2:
                        print("You win the game!!!")
                        dead = True
                    else:
                        print("You live to fight another day")
                else:
                    dead = True 
                    print("Game over!")
            else:
                print("You don't have a " + combat_item)
    elif command == "bribe":
        if inhabitant is not None:
            cash = int(input("How are going to bribe with!"))
            survive = inhabitant.bribe(cash)
            if survive:
                if inhabitant.enemies_defeated == 2:
                    print("You win the game!!!")
                    dead = True
                else:
                    print("You live to fight another day")
            else:
                print("Game over!")
                dead = True
    elif command == "borrow":
        if inhabitant is not None:
            cash = inhabitant.borrow_money()
    elif command == "take":
        if item_present is not None:
            backpack.append(item_present.get_name())
            print("You take the " + item_present.get_name())
            current_room.set_item(None)
    elif command == "backpack":
        if not backpack:
            print("The backpage is empty")
        else:
            print("The backpage contains:")
            for stuff in backpack:
                print(stuff)
                
            