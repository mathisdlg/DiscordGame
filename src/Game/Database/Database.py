from os.path import exists
from os import mkdir
import pickle


class GameDB:

    def __init__(self):
        """
        ##Game name##'s  database
        """
        pass
    
    def connect(self, file_name):
        if exists("donnes"):
            if exists("donnes/"+file_name):
                self.pick = open("donnes/"+file_name, "r+b")
                return 0
        else:
            mkdir("donnes") 
        self.pick = open("donnes/"+file_name, "w+b")
        self.save([])
        return 1
    
    def save(self, object):
        self.pick.seek(0)
        pickle.dump(object, self.pick)
        self.pick.truncate()
        return 0
    
    def load(self):
        self.pick.seek(0)
        list_players = pickle.load(self.pick)
        return list_players
        
    def disconnect(self):
        self.pick.close()
        return 0


if __name__ == "__main__":
    pass