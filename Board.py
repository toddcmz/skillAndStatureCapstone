from random import shuffle

class Board_Template():

    def __init__(self):
        # this is the graph of all nodes and edges, where nodes are sites
        # and edges are either internal or border. Sites are numbered based on
        # a drawing I made of the board. idea is specific site type data will get
        # assigned by looping through a list of shuffled sites and adding that information
        # to each node (site) during board creating when we're playing the game.

        self.region_bonuses = {1: None, 2: None, 3: None, 4: None} # this will get filled out with actual bonuses during board creation

        # regionbonuses are going to be really hard to implement, might not add that functionality until very end
        #
        self.region_deck = [ # this is the deck of region bonuses that will get dealt randomly
            {"Hitchhiking" : ""},
            {"Diplomacy" : ""},
            {"Boasting" : ""},
            {"Sneaky Knave" : ""},
            {"Souvenir" : ""},
            {"Proletariat" : ""},
            {"Public Works" : ""},
            {"Ingenuity" : ""}
        ]

        self.site_deck = [ # this is the deck of sites that will get dealt randomly across the board
            {"site_cat" : "guild",
             "site_name": "alchemists",
             "visiting": [],
             "travel_cost": 3
            },
            {"site_cat" : "guild",
             "site_name": "merchants",
             "visiting": [],
             "travel_cost": 3
            },
            {"site_cat" : "guild",
             "site_name": "craftsmen",
             "visiting": [],
             "travel_cost": 3
            },
            {"site_cat" : "village",
             "site_name": "purple",
             "visiting": [],
             "travel_cost": 1,
             "active" : False
            },
            {"site_cat" : "village",
             "site_name": "green",
             "visiting": [],
             "travel_cost": 1,
             "active" : False
            },
            {"site_cat" : "village",
             "site_name": "white",
             "visiting": [],
             "travel_cost": 1,
             "active" : False
            },
            {"site_cat" : "village",
             "site_name": "yellow",
             "visiting": [],
             "travel_cost": 1,
             "active" : False
            },
            {"site_cat" : "village",
             "site_name": "blue",
             "visiting": [],
             "travel_cost": 1,
             "active" : False
            },
            {"site_cat" : "resource",
             "site_name": "plains",
             "producing": [],
             "visiting": [],
             "travel_cost": 1
            },
            {"site_cat" : "resource",
             "site_name": "plains",
             "producing": [],
             "visiting": [],
             "travel_cost": 2
            },
            {"site_cat" : "resource",
             "site_name": "plains",
             "producing": [],
             "visiting": [],
             "travel_cost": 2
            },
            {"site_cat" : "resource",
             "site_name": "plains",
             "producing": [],
             "visiting": [],
             "travel_cost": 3
            },
            {"site_cat" : "resource",
             "site_name": "forests",
             "producing": [],
             "visiting": [],
             "travel_cost": 1
            },
            {"site_cat" : "resource",
             "site_name": "forests",
             "producing": [],
             "visiting": [],
             "travel_cost": 2
            },
            {"site_cat" : "resource",
             "site_name": "forests",
             "producing": [],
             "visiting": [],
             "travel_cost": 2
            },
            {"site_cat" : "resource",
             "site_name": "forests",
             "producing": [],
             "visiting": [],
             "travel_cost": 3
            },
            {"site_cat" : "resource",
             "site_name": "mountains",
             "producing": [],
             "visiting": [],
             "travel_cost": 1
            },
            {"site_cat" : "resource",
             "site_name": "mountains",
             "producing": [],
             "visiting": [],
             "travel_cost": 2
            },
            {"site_cat" : "resource",
             "site_name": "mountains",
             "producing": [],
             "visiting": [],
             "travel_cost": 2
            },
            {"site_cat" : "resource",
             "site_name": "mountains",
             "producing": [],
             "visiting": [],
             "travel_cost": 3
            }
        ]

        self.sites= { # these are fixed board locations, nodes
            1 : {
                "region" : 1,
                "internal" : [2,4],
                "border" : [11]
            },
            2 : {
                "region" : 1,
                "internal" : [1,3,4,5],
                "border" : [18]
            },
            3 : {
                "region" : 1,
                "internal" : [2,5],
                "border" : [6]
            },
            4 : {
                "region" : 1,
                "internal" : [1,2,5],
                "border" : [13]
            },
            5 : {
                "region" : 1,
                "internal" : [2,3,4],
                "border" : [8,17]
            },
            6 : {
                "region" : 2,
                "internal" : [7,8],
                "border" : [3]
            },
            7 : {
                "region" : 2,
                "internal" : [6,8,9,10],
                "border" : [12]
            },
            8 : {
                "region" : 2,
                "internal" : [6,7,10],
                "border" : [5,17]
            },
            9 : {
                "region" : 2,
                "internal" : [7,10],
                "border" : [14]
            },
            10 : {
                "region" : 2,
                "internal" : [7,8,9],
                "border" : [20]
            },
            11 : {
                "region" : 3,
                "internal" : [12,13,14],
                "border" : [1]
            },
            12 : {
                "region" : 3,
                "internal" : [11,14],
                "border" : [7]
            },
            13 : {
                "region" : 3,
                "internal" : [11,14,15],
                "border" : [4,16]
            },
            14 : {
                "region" : 3,
                "internal" : [11,12,13,15],
                "border" : [9]
            },
            15 : {
                "region" : 3,
                "internal" : [13,14],
                "border" : [19]
            },
            16 : {
                "region" : 4,
                "internal" : [17,18,19],
                "border" : [13]
            },
            17 : {
                "region" : 4,
                "internal" : [16,18,20],
                "border" : [5,8]
            },
            18 : {
                "region" : 4,
                "internal" : [16,17,19,20],
                "border" : [2]
            },
            19 : {
                "region" : 4,
                "internal" : [16,18],
                "border" : [15]
            },
            20 : {
                "region" : 4,
                "internal" : [17,18],
                "border" : [10]
            } 
        }

    def generate_board(self): # this randomly deals site deck locations to each fixed board node (site)
        shuffle(self.site_deck)
        # I numbered the sites 1 to 20 instead of 0 to 19, so I have to add 1 to the indexes
        # to get the right site number in the site dictionary
        for i in range(len(self.site_deck)):
            self.sites[i+1]["site_data"] = self.site_deck[i]
        print("done assigning sites to board")

    def assign_region_bonuses(self): # this randomly assigns region bonuses to the board
        shuffle(self.region_deck)
        for ele in range(1,5):
            self.region_bonuses[ele] = self.region_deck.pop()
        print(self.region_bonuses)
        print("done assigning region bonuses to board")

    def find_home_village(self, target_color): # this is to help place workers at game start, but may have other uses
        for node in self.sites:
            if self.sites[node]["site_data"]["site_name"] == target_color:
                return(node)