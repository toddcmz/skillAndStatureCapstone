from random import shuffle

class Market():
    
    def __init__(self):
        self.supply_gambits = []
        self.discard_gambits = []
        self.market_gambits = []
        self.craftsmen_tools = []
        self.merchants_tools = []
        self.alchemists_tools = []

    def market_set_up(self, num_players):
        # fill out supply deck for gambits
        # assign number of each card
        gambit_counts = {"letter" : 4,"contract" : 4,"shoes" : 4,"fish" : 4,"rod" : 4,
                         "vacation" : 5,"coffee" : 5,"sacks": 5,"maps" : 5}
        # generate full list of gambits appearing in the deck
        for this_card,this_number in gambit_counts.items():
            self.supply_gambits.extend([this_card]*this_number)
        # shuffle the supply deck of gambits for this game
        shuffle(self.supply_gambits)
        # fill in gambits from the supply for purchase
        self.stock_market()
        print("done with gambit setup")

        # fill out the tools
        tools = ["catalyst", "crucible", "ledger", "rope", "bellows", "grindstone"] * num_players
        shuffle(tools)
        break_point = int(len(tools)/3)
        self.craftsmen_tools.extend(tools[0:break_point])
        self.merchants_tools.extend(tools[break_point:break_point+break_point])
        self.alchemists_tools.extend(tools[break_point+break_point:])
        print("done with tools setup")

    def stock_market(self):
        while len(self.market_gambits) < 5: # fill in the gaps in market up to 5 gambits, call at end of player's turn
            self.market_gambits.append(self.supply_gambits.pop())
        print("Market gambits restocked")

    def shuffle_discards(self):
        pass

