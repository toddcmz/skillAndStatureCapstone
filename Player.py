import Workforce
import Board
class Player():

    def __init__(self, color):
        # player color
        self.color = color
        self.resources = {
            'flax' : {"raw" : 0, "refined" : 0},
            'ore' : {"raw" : 0, "refined" : 0},
            'lumber' : {"raw" : 0, "refined" : 0},
        }
        self.tools = {
            'crucible' : False,
            'catalyst' : False,
            'rope' : False,
            'ledger' : False,
            'grindstone' : False,
            'bellows' : False
        }
        self.upgrades = {
            "athanor" : False,
            "writ" : False,
            "furnace" : False
        }
        self.gambits = []

        self.worker1 = Workforce(self.color, "worker")
        self.worker2 = Workforce(self.color, "worker")
        self.worker3 = Workforce(self.color, "worker")
        self.worker4 = Workforce(self.color, "worker")
        self.worker5 = Workforce(self.color, "worker")
        self.artisan1 = Workforce(self.color, "artisan")
        self.artisan2 = Workforce(self.color, "artisan")

        self.worker_list = [self.worker1, self.worker2, self.worker3, self.worker4, self.worker5]
        self.artisan_list = [self.artisan1, self.artisan2]

        self.skills = {
            "alchemists" : "apprentice",
            "merchants" : "apprentice",
            "craftsmen" : "apprentice"
        }
        self.travel_remaining = 7
        self.actions_taken = []
        self.stature = 0

    def take_turn_main(self):
        pass

    def player_produce(self):
        pass

    def player_refine(self):
        pass

    def player_market(self):
        pass

    def player_develop(self):
        pass

    def player_commission(self):
        pass

    def player_travel(self):
        pass

    def player_uses_gambit(self):
        pass

    def player_ends_turn(self):
        pass
