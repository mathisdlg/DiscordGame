DIFFICULTY_LIST = ["G", "F", "E", "D", "C", "B", "A", "S", "2S", "3S"]

class Tower:
    def __init__(self, level: int, difficulty: str) -> None:
        self.level = level
        self.difficulty = difficulty
        