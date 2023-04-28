import player
import Board
import commissions
import gambits
import market

class New_Game():

    def __init__(self, num_players):
        self.num_players = num_players
        self.active_player_list = []

    def main(self):
        pass

    def choose_color(self): # this needs to interact with players to know how many are playing. Writing manual for now.
        blue_player = player("blue")
        white_player = player("white")
        self.active_player_list.append(blue_player)
        self.active_player_list.append(white_player)

    def turn_order(self):
        pass

    # this deals out sites randomly to all spots on the board and chooses this game's region bonuses
    def set_up_board(self):
        self.game_board = Board.Board_Template()
        self.game_board.generate_board()
        self.game_board.assign_region_bonuses()

    # deals starting gambits and tools to market
    def set_up_market(self):
        self.game_market = market.Market()
        self.game_market.market_set_up(self.num_players)

    # this is only partially built at the moment, loops through player colors and gets player pieces in correct home village at game start
    def player_starting_workforce_placement(self): 
        for this_player in self.active_player_list:
            home_location = self.game_board.find_home_village(this_player.color)
            this_player.worker1.location = this_player.worker2.location = this_player.artisan1.location = home_location
            this_player.worker1.location_type = this_player.worker2.location_type = this_player.artisan1.location_type = "home_village"
            
    def start_play(self):
        pass
