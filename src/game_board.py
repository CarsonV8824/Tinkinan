import networkx as nx
import random


class GameBoard:

    def __init__(self):
        
        self.graph = nx.Graph()
        
        self.tiles = {"Fields":4, "Forest":4, "Pasture":4, "Hills":3, "Mountains":3, "Desert":1}

        
        while True:
            chossen = random.choice(list(self.tiles.keys()))
            if self.tiles[chossen] > 0:
                self.graph.add_node(chossen)
                self.tiles[chossen] -= 1
            
            if (check := self.tiles.values()) == (0,0,0,0,0):
                break


    def __str__(self):
        return f"{self.graph.nodes}"


if __name__ == "__main__":
    game = GameBoard()
    print(game)