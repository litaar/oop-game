class Map:
    # Add constructor to class
    def __init__(self, map_name, map_description):
        # Add setter and getter methods to allow characters to be added to map
    def set_character(self,player):
        self.character = input()
    def get_character(self,player):
        return self.character
    # Method to get the description of setting:
    def get_description(self):
        return self.description

    # Here is a method to set the description of the cave:
    def set_description(self, map_description):
        self.description = map_description


map = default(default_name: "sunny day",default_description: "it's a sunny day with clear skies!")