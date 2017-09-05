class Item():
    def __init__(self,item_name):
        self.name = item_name
        self.description = None
        
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name
    
    def set_description(self,description):
        self.description = description
        
    def get_description(self):
        return self.description

    def get_details(self):
        print(self.description)
    

