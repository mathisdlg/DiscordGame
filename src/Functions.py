from Game.Class import Class, CLASS_LIST, choose_class
from Game.Race import Race, RACE_LIST, choose_race
from Game.Player import Player
from Game.Skill import Skill

from os import system, name 



def choose_name(Name_list):
    while True:
        name_ = input("Enter your pseudo: ")
        if name_ not in Name_list:
            return name_


def add_player(Name_list, Player_list):
    name = choose_name(Name_list)
    
    clear_output()        
    race_chooser = choose_race()
    
    clear_output()
    class_chooser = choose_class()

    Name_list.append(name)
    Player_list.append(Player(name, Class(class_chooser), Race(race_chooser)))

def suppr_player(name_list, Player_list):
    player_name = input("Enter a player name: ")
    if player_name not in name_list:
        return 1
    else:
        del Player_list[name_list.index(player_name)]
        name_list.remove(player_name)
        return 0

def get_player(Player_list, Name_list):
    while True:
        name = input("Enter a player name: ")
        if name in Name_list:
            print("Player found!")
            return Player_list[Name_list.index(name)]
        else:
            print("Player not found")

def print_player(Player:Player):
    print(f"Player: {Player.get_name()} is level is {Player.get_level()} and he have {Player.get_stat_point()} stat points\n")

def print_all_player(Player_list):
    for Player in Player_list:
        print_player(Player)
    return len(Player_list)

def generate_list_name(player_list):
    return [player.get_name() for player in player_list]


def clear_output():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def load_all_combine(CL, RL):
    i = 0
    for class_ in CL:
        for race_ in RL:
            print(f"A {race_} of class: {class_}")
            i+=1
    return i

def display_player(Player_list, Name_list):
    player = get_player(Player_list, Name_list)

    if player == 0:
        return 0
    else:
        print("=============="+"="*len(player.name))
        print(f"Player name: {player.name}")
        print("=============="+"="*len(player.name))