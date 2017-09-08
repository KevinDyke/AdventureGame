class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
class Enemy(Character):

     def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.bribe_limit = None
        
     def get_weakness(self):
        return self.weakness
    
     def set_weakness(self,weakness):
         self.weakness = weakness
         
     def fight(self, combat_item):
         if combat_item == self.weakness:
             print("You fend " + self.name + " off with the " + combat_item )
             return True
         else:
             print(self.name + " crushes you, puny adventurer")
             return False

     def set_bribe(self,amount):
         self.bribe_limit = amount
         
     def get_bribe(self):
         return self.bribe_limit
     
     def bribe(self,cash):
         if cash >= self.bribe_limit:
             print("You bribed " + self.name + " off with the bribe of " + str(cash) )
             return True
         else:
             print(self.name + " crushes you, puny adventurer")
             return False
             
class Friend(Character):
     
     def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.cash_limit = None
        
     def set_cash(self,amount):
        self.cash_limit = amount
        
     def get_cash(self):
         return self.cash_limit
     
     def borrow_money(self):
         amount = self.cash_limit
         print(self.name + " lends you " + str(self.cash_limit))
         self.cash_limit = 0
         return amount
     




    
    
