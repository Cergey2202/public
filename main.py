# -*- coding: utf-8 -*-

from typing import List, Dict
import obj
from random import choice
a= [
    [obj.Air(), obj.Air(), obj.Air(), obj.Air(), obj.Air()],
    [obj.Air(), obj.Air(), obj.Air(), obj.Air(), obj.Air()],
    [obj.Air(), obj.Air(), obj.Player("Steve", 20, 5, "P"), obj.Air(), obj.Air()],
    [obj.Air(), obj.Air(), obj.Air(), obj.Air(), obj.Air()],
    [obj.Air(), obj.Air(), obj.Air(), obj.Air(), obj.Air()],
]

class Map:
    def __init__(self, map: list) -> None:
        self.map= map

    def generate(self, h: int, chances: dict) -> List[List[str]]:
        self.temp_map_s= []
        for self.a, self.b in chances.items(): self.temp_map_s+= list(self.a*self.b)
        self.temp_map= []
        for x in range(h*h): self.temp_map.append(choice(self.temp_map_s))
        self.temp1= []  
        self.temp2= []
        for self.char in self.temp_map:
            if len(self.temp1) != h: self.temp1.append(self.char)
            else: self.temp2.append(self.temp1); self.temp1= []
        return self.temp2
        
    def get_map_display(self, str_mode: bool = False) -> List[List[str]]:
        self.temp_map= []
        for self.line in self.map:
            self.temp_list= []
            self.temp_map.append([ self.block.obj for self.block in self.line])
        return self.temp_map if not str_mode else "\n".join(("".join(self.block)) for self.block in self.temp_map)
        
    def set_block(self, cords: tuple, block) -> None:
        self.map[cords[0]][cords[1]]= block()

    def get_block(self, cords: tuple) -> obj.types.Block: return  self.map[cords[0]][cords[1]]
    
    def get_player_location(self, player: obj.types.Player):


b= Map(a)
