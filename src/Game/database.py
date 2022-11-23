from os.path import exists
from Game.Player import Player
import pickle


class GameDB:

    def __init__(self):
        pass
    
    def connect(self, file_name):
        if exists(file_name):
            self.pick = open(file_name, "r+b")
        else:
            self.pick = open(file_name, "wb+")
            self.save([])
    
    def save(self, object):
        self.pick.seek(0)
        pickle.dump(object, self.pick)
    
    def load(self):
        self.pick.seek(0)
        tmp = pickle.load(self.pick)
        return tmp
        
    def disconnect(self):
        self.pick.close()


if __name__ == "__main__":
    pass