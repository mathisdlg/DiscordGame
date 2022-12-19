from Game.Player import Player

STATE_LIST = ["opened", "closed", "invited", "complet"]

class Clan:
    
    def __init__(self, name:str, master:Player):
        self.name = name
        self.master = master
        self.experince = 0
        self.level = 0
        self.places = 11
        self.list_players = [master]
    
    def get_name(self):
        return self.name
    
    def get_master(self):
        return self.master
    
    def get_experince(self):
        return self.experince
    
    def get_level(self):
        return self.level
    
    def _get_place(self):
        return self.places
    
    def get_free_place(self):
        return self._get_place() - len(self.list_players)
    
    def get_list_players(self):
        return self.list_players
    
    def add_player(self, player:Player):
        if player in self.list_players:
            return 1
        elif player.get_clan() != None:
            self.list_players.append(player)
            player.set_clan(self.name)
            return 0
        else:
            return 4
    
    def remove_player(self, player:Player):
        if player in self.list_players:
            self.list_players.remove(player)
            return 0
        else:
            return 2
        
    def set_state(self, state):
        if state in STATE_LIST:
            self.state = state
            return 0
        else: 
            return 3