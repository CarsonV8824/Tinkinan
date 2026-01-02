import networkx as nx
from collections import deque
import random

import player

class GameStruct:

    def __init__(self):
        
        self.graph = nx.Graph()
        
        self.dice_numbers = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]
        #self.dice_numbers = deque(self.dice_numbers)
        #self.dice_numbers.rotate(random.randint(-len(self.dice_numbers), len(self.dice_numbers)))
        #self.dice_numbers = list(self.dice_numbers)

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

            
            self.graph.add_node(f"Piece{i}", Resource=None, dice_number=None)
        
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

        self.graph.add_edge("House7", "Piece4")
        self.graph.add_edge("House8", "Piece4")
        self.graph.add_edge("House9", "Piece4")
        self.graph.add_edge("House34", "Piece4")
        self.graph.add_edge("House35", "Piece4")
        self.graph.add_edge("House36", "Piece4")
        #---piece 5---

        self.graph.add_edge("House9", "Piece5")
        self.graph.add_edge("House10", "Piece5")
        self.graph.add_edge("House11", "Piece5")
        self.graph.add_edge("House12", "Piece5")
        self.graph.add_edge("House36", "Piece5")
        self.graph.add_edge("House37", "Piece5")

        #--piece 6---

        self.graph.add_edge("House12", "Piece6")
        self.graph.add_edge("House13", "Piece6")
        self.graph.add_edge("House14", "Piece6")
        self.graph.add_edge("House37", "Piece6")
        self.graph.add_edge("House38", "Piece6")
        self.graph.add_edge("House39", "Piece6")

        #---piece 7---

        self.graph.add_edge("House14", "Piece7")
        self.graph.add_edge("House15", "Piece7")
        self.graph.add_edge("House16", "Piece7")
        self.graph.add_edge("House17", "Piece7")
        self.graph.add_edge("House39", "Piece7")
        self.graph.add_edge("House40", "Piece7")

        #---piece 8---

        self.graph.add_edge("House17", "Piece8")
        self.graph.add_edge("House18", "Piece8")
        self.graph.add_edge("House19", "Piece8")
        self.graph.add_edge("House40", "Piece8")
        self.graph.add_edge("House41", "Piece8")
        self.graph.add_edge("House42", "Piece8")
        
        #---piece 9---

        self.graph.add_edge("House19", "Piece9")
        self.graph.add_edge("House20", "Piece9")
        self.graph.add_edge("House21", "Piece9")
        self.graph.add_edge("House22", "Piece9")
        self.graph.add_edge("House42", "Piece9")
        self.graph.add_edge("House43", "Piece9")

        #--piece 10---

        self.graph.add_edge("House22", "Piece10")
        self.graph.add_edge("House23", "Piece10")
        self.graph.add_edge("House24", "Piece10")
        self.graph.add_edge("House43", "Piece10")
        self.graph.add_edge("House44", "Piece10")
        self.graph.add_edge("House45", "Piece10")

        #--piece 11---

        self.graph.add_edge("House24", "Piece11")
        self.graph.add_edge("House25", "Piece11")
        self.graph.add_edge("House26", "Piece11")
        self.graph.add_edge("House27", "Piece11")
        self.graph.add_edge("House45", "Piece11")
        self.graph.add_edge("House46", "Piece11")
        #---piece 12---

        self.graph.add_edge("House27", "Piece12")
        self.graph.add_edge("House28", "Piece12")
        self.graph.add_edge("House29", "Piece12")
        self.graph.add_edge("House46", "Piece12")
        self.graph.add_edge("House47", "Piece12")
        self.graph.add_edge("House48", "Piece12")
        
        #---piece 13---

        self.graph.add_edge("House31", "Piece13")
        self.graph.add_edge("House32", "Piece13")
        self.graph.add_edge("House47", "Piece13")
        self.graph.add_edge("House48", "Piece13")
        self.graph.add_edge("House49", "Piece13")
        self.graph.add_edge("House54", "Piece13")

        #---piece 14---

        self.graph.add_edge("House32", "Piece14")
        self.graph.add_edge("House33", "Piece14")
        self.graph.add_edge("House34", "Piece14")
        self.graph.add_edge("House35", "Piece14")
        self.graph.add_edge("House49", "Piece14")
        self.graph.add_edge("House50", "Piece14")
        #---piece 15---

        self.graph.add_edge("House35", "Piece15")
        self.graph.add_edge("House36", "Piece15")
        self.graph.add_edge("House37", "Piece15")
        self.graph.add_edge("House38", "Piece15")
        self.graph.add_edge("House50", "Piece15")
        self.graph.add_edge("House51", "Piece15")

        #---piece 16---

        self.graph.add_edge("House38", "Piece16")
        self.graph.add_edge("House39", "Piece16")
        self.graph.add_edge("House40", "Piece16")
        self.graph.add_edge("House41", "Piece16")
        self.graph.add_edge("House51", "Piece16")
        self.graph.add_edge("House52", "Piece16")
        

        #---piece 17---

        self.graph.add_edge("House41", "Piece17")
        self.graph.add_edge("House42", "Piece17")
        self.graph.add_edge("House43", "Piece17")
        self.graph.add_edge("House44", "Piece17")
        self.graph.add_edge("House52", "Piece17")
        self.graph.add_edge("House53", "Piece17")

        #---piece 18---

        self.graph.add_edge("House44", "Piece18")
        self.graph.add_edge("House45", "Piece18")
        self.graph.add_edge("House46", "Piece18")
        self.graph.add_edge("House47", "Piece18")
        self.graph.add_edge("House53", "Piece18")
        self.graph.add_edge("House54", "Piece18")
        
        #---piece 19---

        self.graph.add_edge("House49", "Piece19")
        self.graph.add_edge("House50", "Piece19")
        self.graph.add_edge("House51", "Piece19")
        self.graph.add_edge("House52", "Piece19")
        self.graph.add_edge("House53", "Piece19")
        self.graph.add_edge("House54", "Piece19")
        
    def add_image_color_to_piece(self, piece_number, resource_type):
        node_name = f"Piece{piece_number}"

        self.graph.nodes[node_name]['Resource'] = resource_type

        if resource_type == "tan" or resource_type == "desert":
            dice_number = ""
            self.graph.nodes[node_name]['dice_number'] = dice_number
        else:
            try:
                choosen_number = self.dice_numbers.pop(0)
            except Exception as e:
                print(e)
            dice_number = choosen_number
            self.graph.nodes[node_name]['dice_number'] = dice_number

        print(f"Added {self.graph.nodes[node_name]['Resource']} with dice number {self.graph.nodes[node_name]['dice_number']}")

    def get_piece_dice_number(self, piece_number):
        node = f"Piece{piece_number}"
        
        return self.graph.nodes[node]['dice_number']
    
    def place_settlement_initial(self, player, board):
        available_houses = [node for node in self.graph.nodes if node.startswith("House") and self.graph.nodes[node]['Player'] is None]
        if available_houses:
            chosen_house = random.choice(available_houses)
            self.graph.nodes[chosen_house]['Player'] = player.name
            self.graph.nodes[chosen_house]['Type'] = "Settlement"
            board.draw_settlement_initial(chosen_house, player.color)
            print(f"{player.name} placed initial settlement at {chosen_house}.")

    def place_road_off_of__init_settlement(self, player, board):
        player_houses = [node for node in self.graph.nodes if node.startswith("House") and self.graph.nodes[node].get('Player') == player.name and self.graph.nodes[node].get('Type') == "Settlement"]
        
        # Place one road for EACH settlement
        for house in player_houses:
            possible_roads = []
            neighbors = self.graph.neighbors(house)
            for neighbor in neighbors:
                # Only consider House nodes as valid road endpoints, not Piece nodes
                if neighbor.startswith("House") and self.graph.nodes[neighbor]['Player'] is None:
                    # Check if the edge doesn't already have a road
                    edge_data = self.graph.get_edge_data(house, neighbor)
                    if edge_data.get('Player') is None:
                        possible_roads.append((house, neighbor))
            
            if possible_roads:
                chosen_road = random.choice(possible_roads)
                # Store road ownership on the EDGE, not the node
                self.graph[chosen_road[0]][chosen_road[1]]['Player'] = player.name
                board.draw_road_initial(chosen_road[0], chosen_road[1], player.color)
                print(f"{player.name} placed road from {chosen_road[0]} to {chosen_road[1]}.")


    def distribute_resources(self, dice_roll, players: list):
        for piece in list(self.graph.nodes):
            if piece.startswith("Piece"):
                piece_data = self.graph.nodes[piece]
                # Convert dice_number to int for comparison, skip if empty string
                dice_number = piece_data['dice_number']
                if dice_number and int(dice_number) == dice_roll:
                    connected_houses = [n for n in self.graph.neighbors(piece) if n.startswith("House")]
                    for house in connected_houses:
                        house_data = self.graph.nodes[house]
                        owner = house_data['Player']
                        if owner:
                            resource = piece_data['Resource']
                            for p in players:
                                if p.name == owner:
                                    p.add_resource(resource, 1)
                                    print(f"{p.name} received 1 {resource} from {piece} due to dice roll {dice_roll}.")
        
    def __str__(self):
        return f"nodes: {len(list(self.graph.nodes))}. number of edges {len(list(self.graph.edges))}"

if __name__ == "__main__":
    game = GameStruct()
    game.add_image_color_to_piece(1, "wood")
    #print(game)