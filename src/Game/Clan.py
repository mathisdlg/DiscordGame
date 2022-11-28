from Game.Player import Player

class Clan:
    
    def __init__(self, name:str, master:Player):
        self.name = name
        self.master = master
        self.experince = 0
        self.level = 0
        self.list_players = [master]
    
    def get_name(self):
        return self.name
    
    def get_master(self):
        return self.master
    
    def get_experince(self):
        return self.experince
    
    def get_level(self):
        return self.level
    
    def get_list_players(self):
        return self.list_players
    
    def add_player(self, player:Player):
        if player in self.list_players:
            return 1
        else:
            self.list_players.append(player)
            return 0
    
    def remove_player(self, player:Player):
        if player in self.list_players:
            self.list_players.remove(player)
        else:
            return 1