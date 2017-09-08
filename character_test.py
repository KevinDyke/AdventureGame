from character import Enemy

dave = Enemy("Dave","A smelly zombie")
dave.set_weakness("cheese")

dave.describe()

dave.set_conversation("Give me your brains!!!")

dave.talk()

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)





