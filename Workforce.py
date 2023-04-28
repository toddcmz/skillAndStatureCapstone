class Workforce():
    def __init__(self, player, type):
        self.player = player
        self.type = type
        self.name = self.player+self.type
        self.location = None # this will be the node number
        self.location_type = None # this will get updated with a method when the piece moves?

    def update_location(self, node_num): # when the peice moves we'll get the location type for the new node for checking commission reqs?
        pass