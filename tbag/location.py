# This will represent the maps the player will play with
class Map:
    # Add constructor to class
    def __init__(self, map_name, map_description):
        # Add link_cave method here
        self.map_name = map_name
        self.description = map_description

         # Here is a method to get the description of the cave:
        def get_description(self):
            return self.description

        # Here is a method to set the description of the cave:
        def set_description(self, map_description):
            self.description = map_description

        def get_name(self):
            return self.map_name

        def set_name(self, map_name):
            self.cave_name = name

        # Give map a description
        def describe(self):
            print(self.get_description())

        # get and print details of cave (name, description, directions)
        def get_details(self):
            print(self.cave_name)
            print(self.description)
            for direction in self.linked_caves:
                cave = self.linked_caves[direction]
                print("The " + cave.get_name() + " is " + direction)

    attribute: health
