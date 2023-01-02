class Object:
    """
    Objet:
        - Sword                     (Weapon)
        - Ring                      (Armor)
        - Katana                    (Weapon)
        - Book                      (Armor)
        - Helmet                    (Armor)
        - Armor                     (Armor)
        - mage staff                (Weapon)
        - wish ring                 (Object)
        - Bow                       (Weapon)
        - Baguette                  (Weapon)
        - Shield                    (Weapon)
        - Boots                     (Armor)
        - Champagne                 (Object)
        - Hat                       (Armor)
        - potion of life            (Object)
        - doppleganger potion       (Object)
        - HP Potion                 (Object)
        - MP Potion                 (Object)
    Bonus stat:
        - 
    """
    def __init__(self, objet_name: str, rarity: str, rangeatk: int, ego: bool):
        self.objet_name = objet_name
        self.rarity = rarity
        self.range = rangeatk
        self.ego = ego