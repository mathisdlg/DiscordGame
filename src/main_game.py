from Game import *

def test():
    len_class = len(Class.CLASS_LIST)
    len_race = len(Race.RACE_LIST)
    print(f"Nombre de possibilité (choix classe x  race): {len_race*len_class}")
    pass

def load_all_combine(CL, RL):
    i = 0
    for class_ in CL:
        for race_ in RL:
            print(f"A {race_} of class: {class_}")
            i+=1
    return i


if __name__ == "__main__":
    print(load_all_combine(Class.CLASS_LIST, Race.RACE_LIST))
    test()