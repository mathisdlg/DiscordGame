from os.path import exists
import pickle


class GameDB:

    def __init__(self):
        """
        Database constructor game's database of ##Game name##
        """
        pass
    
    def connect(self, file_name):
        if exists(file_name):
            self.pick = open(file_name, "r+b")
            return 0
        else:
            self.pick = open(file_name, "x+b")
            self.save([])
            return 1
    
    def save(self, object):
        self.pick.seek(0)
        pickle.dump(object, self.pick)
        self.pick.truncate()
        return 0
    
    def load(self):
        self.pick.seek(0)
        tmp = pickle.load(self.pick)
        return tmp
        
    def disconnect(self):
        self.pick.close()


if __name__ == "__main__":
    pass