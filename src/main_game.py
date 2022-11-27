from Test import *



if __name__ == '__main__':
    db = GameDB()
    db.connect("donnes/db.pickle")

    Player_list = []
    Player_list = db.load()
    
    Name_list = generate_list_name(Player_list)
    print("Hello, World!")
    
    clear_output()

    while True:
        choose = int(input("\n[1] - New character\n[2] - Remove a character\n[3] - Save changes\n[4] - Load Player\n[5] - Print all player\n[8] - See all Class Race combination\n[9] - Exit\n"))
        
        clear_output()
        
        if choose == 1:
            add_player(Player_list, Player_list)

        elif choose == 2:
            if suppr_player(Name_list, Player_list) == 0:
                print("Player has been deleted\n")
            else:
                print("Error: Player cannot be found\n")
            input("Press in enter to continue...")

        elif choose == 3:
            db.save(Player_list)
            print("Player saved!")
            input("Press in enter to continue...")

        elif choose == 4:
            Player_list = db.load()
            print("Player load!")
            input("Press in enter to continue...")

        elif choose == 5:
            print_all_player(Player_list)
            input("Press in enter to continue...")
        
        elif choose == 6:
            pass

        elif choose == 8:
            print(f"{load_all_combine(CLASS_LIST, RACE_LIST)} possilities")
            input("Press in enter to continue...")

        elif choose == 9:
            print("Exit...")
            db.disconnect()
            break

    print("Goodbye!")