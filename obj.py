class types:
    Player= "Player"
    Block= "Block"
class Player:
    def __init__(self, name: str, hp: int, damage: int, obj: str) -> None:
        self.type= types.Player
        self.name= name
        self.hp= hp
        self.damage= damage
        self.obj= obj
        self.hand= None
        self.inventory= []

class Tree:
    def __init__(self) -> None:
        self.type= types.Block
        self.name= "Tree"
        self.obj= "T"

class Air:
    def __init__(self) -> None:
        self.type= types.Block
        self.name= "Air"
        self.obj= "A"