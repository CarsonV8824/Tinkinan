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
        
        #---connect the rest of the houses---

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

        self.graph.add_edge("House27", "Piece4")
        self.graph.add_edge("House28", "Piece4")
        self.graph.add_edge("House29", "Piece4")
        self.graph.add_edge("House46", "Piece4")
        self.graph.add_edge("House47", "Piece4")
        self.graph.add_edge("House48", "Piece4")

        #---piece 5---

        self.graph.add_edge("House31", "Piece5")
        self.graph.add_edge("House32", "Piece5")
        self.graph.add_edge("House47", "Piece5")
        self.graph.add_edge("House48", "Piece5")
        self.graph.add_edge("House49", "Piece5")
        self.graph.add_edge("House54", "Piece5")

        #--piece 6---

        self.graph.add_edge("House32", "Piece6")
        self.graph.add_edge("House33", "Piece6")
        self.graph.add_edge("House34", "Piece6")
        self.graph.add_edge("House35", "Piece6")
        self.graph.add_edge("House49", "Piece6")
        self.graph.add_edge("House50", "Piece6")

        #---piece 7---

        self.graph.add_edge("House7", "Piece7")
        self.graph.add_edge("House8", "Piece7")
        self.graph.add_edge("House9", "Piece7")
        self.graph.add_edge("House34", "Piece7")
        self.graph.add_edge("House35", "Piece7")
        self.graph.add_edge("House36", "Piece7")

        #---piece 8---

        self.graph.add_edge("House24", "Piece8")
        self.graph.add_edge("House25", "Piece8")
        self.graph.add_edge("House26", "Piece8")
        self.graph.add_edge("House27", "Piece8")
        self.graph.add_edge("House45", "Piece8")
        self.graph.add_edge("House46", "Piece8")

        #---piece 9---

        self.graph.add_edge("House44", "Piece9")
        self.graph.add_edge("House45", "Piece9")
        self.graph.add_edge("House46", "Piece9")
        self.graph.add_edge("House47", "Piece9")
        self.graph.add_edge("House53", "Piece9")
        self.graph.add_edge("House54", "Piece9")

        #--piece 10---

        self.graph.add_edge("House49", "Piece10")
        self.graph.add_edge("House50", "Piece10")
        self.graph.add_edge("House51", "Piece10")
        self.graph.add_edge("House52", "Piece10")
        self.graph.add_edge("House53", "Piece10")
        self.graph.add_edge("House54", "Piece10")

        #--piece 11---

        self.graph.add_edge("House35", "Piece11")
        self.graph.add_edge("House36", "Piece11")
        self.graph.add_edge("House37", "Piece11")
        self.graph.add_edge("House38", "Piece11")
        self.graph.add_edge("House50", "Piece11")
        self.graph.add_edge("House51", "Piece11")

        #---piece 12---
        
        self.graph.add_edge("House9", "Piece12")
        self.graph.add_edge("House10", "Piece12")
        self.graph.add_edge("House11", "Piece12")
        self.graph.add_edge("House12", "Piece12")
        self.graph.add_edge("House36", "Piece12")
        self.graph.add_edge("House37", "Piece12")

        #---piece 13---

        self.graph.add_edge("House22", "Piece13")
        self.graph.add_edge("House23", "Piece13")
        self.graph.add_edge("House24", "Piece13")
        self.graph.add_edge("House43", "Piece13")
        self.graph.add_edge("House44", "Piece13")
        self.graph.add_edge("House45", "Piece13")

        #---piece 14---

        self.graph.add_edge("House41", "Piece14")
        self.graph.add_edge("House42", "Piece14")
        self.graph.add_edge("House43", "Piece14")
        self.graph.add_edge("House44", "Piece14")
        self.graph.add_edge("House52", "Piece14")
        self.graph.add_edge("House53", "Piece14")

        #---piece 15---

        self.graph.add_edge("House38", "Piece15")
        self.graph.add_edge("House39", "Piece15")
        self.graph.add_edge("House40", "Piece15")
        self.graph.add_edge("House41", "Piece15")
        self.graph.add_edge("House51", "Piece15")
        self.graph.add_edge("House52", "Piece15")

        #---piece 16---

        self.graph.add_edge("House12", "Piece16")
        self.graph.add_edge("House13", "Piece16")
        self.graph.add_edge("House14", "Piece16")
        self.graph.add_edge("House37", "Piece16")
        self.graph.add_edge("House38", "Piece16")
        self.graph.add_edge("House39", "Piece16")

        #---piece 17---

        self.graph.add_edge("House19", "Piece17")
        self.graph.add_edge("House20", "Piece17")
        self.graph.add_edge("House21", "Piece17")
        self.graph.add_edge("House22", "Piece17")
        self.graph.add_edge("House42", "Piece17")
        self.graph.add_edge("House43", "Piece17")

        #---piece 18---

        self.graph.add_edge("House17", "Piece18")
        self.graph.add_edge("House18", "Piece18")
        self.graph.add_edge("House19", "Piece18")
        self.graph.add_edge("House40", "Piece18")
        self.graph.add_edge("House41", "Piece18")
        self.graph.add_edge("House42", "Piece18")

        #---piece 19---

        self.graph.add_edge("House14", "Piece19")
        self.graph.add_edge("House15", "Piece19")
        self.graph.add_edge("House16", "Piece19")
        self.graph.add_edge("House17", "Piece19")
        self.graph.add_edge("House39", "Piece19")
        self.graph.add_edge("House40", "Piece19")
        
    def add_image_color_to_piece(self, piece_number, resource_type):
        node_name = f"Piece{piece_number}"

        self.graph.nodes[node_name]['Resource'] = resource_type
        
            
    def __str__(self):
        return f"nodes: {len(list(self.graph.nodes))}. number of edges {len(list(self.graph.edges))}"

if __name__ == "__main__":
    game = GameStruct()
    game.add_image_color_to_piece(1, "wood")
    #print(game)