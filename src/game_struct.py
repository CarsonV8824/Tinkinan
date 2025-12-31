import networkx as nx
import random


class GameStruct:

    def __init__(self):
        
        self.graph = nx.Graph()
        
        #---adds all of the places where a person can place a house or road. Use reference photo (Game_Board.png)---
        
        for i in range(1, 55):
            self.graph.add_node(f"House{i}", Player=None, Type=None)
            if 1 < i < 30:
                self.graph.add_edge(f"House{i-1}", f"House{i}", Player=None)
            elif i == 30:
                self.graph.add_edge(f"House{i-1}", f"House{i}", Player=None)
                self.graph.add_edge("House1", f"House{i}", Player=None)
            elif 31 < i < 48:
                self.graph.add_edge(f"House{i-1}", f"House{i}", Player=None)
            elif i == 48:
                self.graph.add_edge(f"House{i}", "House31", Player=None)
                self.graph.add_edge(f"House{i}", f"House{i-1}", Player=None)
            elif 49 < i < 54:
                self.graph.add_edge(f"House{i-1}", f"House{i}", Player=None)
            if i == 54:
                self.graph.add_edge(f"House{i-1}", f"House{i}", Player=None)
                self.graph.add_edge(f"House{i}", "House49", Player=None)
        
        #---Add extra edges as in your original code---

        self.graph.add_edge("House2", "House31", Player=None)
        self.graph.add_edge("House4", "House33", Player=None)
        self.graph.add_edge("House7", "House34", Player=None)
        self.graph.add_edge("House9", "House36", Player=None)
        self.graph.add_edge("House12", "House37", Player=None)
        self.graph.add_edge("House14", "House39", Player=None)
        self.graph.add_edge("House17", "House40", Player=None)
        self.graph.add_edge("House19", "House42", Player=None)
        self.graph.add_edge("House22", "House43", Player=None)
        self.graph.add_edge("House24", "House45", Player=None)
        self.graph.add_edge("House27", "House46", Player=None)
        self.graph.add_edge("House29", "House48", Player=None)

        self.graph.add_edge("House49", "House32", Player=None)
        self.graph.add_edge("House50", "House35", Player=None)
        self.graph.add_edge("House51", "House38", Player=None)
        self.graph.add_edge("House52", "House41", Player=None)
        self.graph.add_edge("House53", "House44", Player=None)
        self.graph.add_edge("House54", "House47", Player=None)

        #---tile pieces themselves---

        for i in range(1, 20):
            self.graph.add_node(f"Piece{i}", Resource=None)
        
        #---piece 1---

        self.graph.add_edge("House1", "Piece1")
        self.graph.add_edge("House2", "Piece1")
        self.graph.add_edge("House31", "Piece1")
        self.graph.add_edge("House48", "Piece1")
        self.graph.add_edge("House29", "Piece1")
        self.graph.add_edge("House30", "Piece1")

        #---piece 2---

        self.graph.add_edge("House2", "Piece2")
        self.graph.add_edge("House3", "Piece2")
        self.graph.add_edge("House4", "Piece2")
        self.graph.add_edge("House33", "Piece2")
        self.graph.add_edge("House32", "Piece2")
        self.graph.add_edge("House31", "Piece2")
        
        #---piece 3---

        self.graph.add_edge("House4", "Piece3")
        self.graph.add_edge("House5", "Piece3")
        self.graph.add_edge("House6", "Piece3")
        self.graph.add_edge("House7", "Piece3")
        self.graph.add_edge("House33", "Piece3")
        self.graph.add_edge("House34", "Piece3")

        #---piece 4---


        





    def test_edge_data(self):
        with open("src/test_edges.txt", "w") as f:
            f.write(str(self.graph.edges))

    def __str__(self):
        return f"nodes: {len(list(self.graph.nodes))}. number of edges {len(list(self.graph.edges))}"

if __name__ == "__main__":
    game = GameStruct()
    game.test_edge_data()
    print(game)