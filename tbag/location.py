#This will represent the maps the player will play with
class Map:
# Add constructor to class
    def __init__(self, map_name, map_description):
        # Add link_cave method here
        self.map_name = map_name
        self.description = map_description
        # Add character attribute here
        self.character = None


    attribute: health