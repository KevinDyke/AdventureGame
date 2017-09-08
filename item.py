
class Item():
    """ describes an item in the adventure game """
    def __init__(self,item_name):
        self.name = item_name
        self.description = None
        
    def get_name(self):
        """ returns the name of the item """
        return self.name
    
    def set_name(self,name):
        """ sets the name of the item """
        self.name = name
    
    def set_description(self,description):
        """ sets the decription of the item """
        self.description = description
        
    def get_description(self):
        """ returns a description of the item """
        return self.description

    def get_details(self):
        """ prints out a copy of the item's description """
        print(self.description)
    

