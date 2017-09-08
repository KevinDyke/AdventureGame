class Character():
    """ super class for characters in the adventure game """
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        """ describes the character """
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """ records what the character will say """
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        """ Makes the character talk """
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        """ fight with the character """
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    """ Describes an enemy in the adventure game """
    enemies_defeated = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.bribe_limit = None

    def get_weakness(self):
        """ returns the enemy weakness """
        return self.weakness

    def set_weakness(self,weakness):
        """ sets the enemy fatal weakness """
        self.weakness = weakness

    def fight(self, combat_item):
        """ combat to death with the enemy """
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            Enemy.enemies_defeated += 1
            print("You have killed " + str(Enemy.enemies_defeated) + " enemies!")
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def set_bribe(self,amount):
        """ sets the amount of money the enemy will take to fake death !!! """
        self.bribe_limit = amount

    def get_bribe(self):
        """ returns the amount of money the enemy will take to fake death !!! """
        return self.bribe_limit

    def bribe(self,cash):
        """ ask the enemy to fake death, if not enought money get killed by enemy """
        if cash >= self.bribe_limit:
            print("You bribed " + self.name + " off with the bribe of " + str(cash) )
            Enemy.enemies_defeated += 1
            print("You have killed " + str(Enemy.enemies_defeated) + " enemies!")
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

class Friend(Character):
    """ A helpful character in the game """
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.cash_limit = None

    def set_cash(self,amount):
        """ sets the amount of money the friend can lend """
        self.cash_limit = amount

    def get_cash(self):
        """ returns the amount of money the friend can lend """
        return self.cash_limit

    def borrow_money(self):
        """ borrow the money from the friend """
        amount = self.cash_limit
        print(self.name + " lends you " + str(self.cash_limit))
        self.cash_limit = 0
        return amount







