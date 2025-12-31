import networkx as nx
import random


class GameStruct:

    def __init__(self):
        
        self.graph = nx.Graph()
        
        for i in range(1, 55):
            if i == 1:
                self.graph.add_node(f"House{i}")
            elif 1 < i < 30:
                self.graph.add_node(f"House{i}")
                
                self.graph.add_edge(f"House{i-1}", f"House{i}", weight={"Player":None})
            elif i == 30:
                self.graph.add_node(f"House{i}")
                
                self.graph.add_edge(f"House{i-1}", f"House{i}", weight={"Player":None})
                self.graph.add_edge("House1", f"House{i}", weight={"Player":None})
            elif i == 31:
                self.graph.add_node(f"House{i}")
            elif 31 < i < 48:
                self.graph.add_node(f"House{i}")
                
                self.graph.add_edge(f"House{i-1}", f"House{i}", weight={"Player":None})
            elif i == 48:
                self.graph.add_node(f"House{i}")
                
                self.graph.add_edge(f"House{i}", "House31", weight={"Player":None})
                self.graph.add_edge(f"House{i}", f"House{i-1}", weight={"Player":None})
            elif i == 49:
                self.graph.add_node(f"House{i}")
            elif 49 < i < 54:
                self.graph.add_node(f"House{i}")
                
                self.graph.add_edge(f"House{i-1}", f"House{i}", weight={"Player":None})
            if i == 54:
                self.graph.add_node(f"House{i}")
                
                self.graph.add_edge(f"House{i-1}", f"House{i}", weight={"Player":None})
                self.graph.add_edge(f"House{i}", "House49", weight={"Player":None})
        
        
        self.graph.add_edge("House2", "House31", weight={"Player":None})
        self.graph.add_edge("House4", "House33", weight={"Player":None})
        self.graph.add_edge("House7", "House34", weight={"Player":None})
        self.graph.add_edge("House9", "House36", weight={"Player":None})
        self.graph.add_edge("House12", "House37", weight={"Player":None})
        self.graph.add_edge("House14", "House39", weight={"Player":None})
        self.graph.add_edge("House17", "House40", weight={"Player":None})
        self.graph.add_edge("House19", "House42", weight={"Player":None})
        self.graph.add_edge("House22", "House43", weight={"Player":None})
        self.graph.add_edge("House24", "House45", weight={"Player":None})
        self.graph.add_edge("House27", "House46", weight={"Player":None})
        self.graph.add_edge("House29", "House48", weight={"Player":None})

        self.graph.add_edge("House49", "House32", weight={"Player":None})
        self.graph.add_edge("House50", "House35", weight={"Player":None})
        self.graph.add_edge("House51", "House38", weight={"Player":None})
        self.graph.add_edge("House52", "House41", weight={"Player":None})
        self.graph.add_edge("House53", "House44", weight={"Player":None})
        self.graph.add_edge("House54", "House47", weight={"Player":None})

    def test_edge_data(self):
        with open("src/test_edges.txt", "w") as f:
            f.write(str(self.graph.edges))

    def __str__(self):
        return f"nodes: {self.graph.nodes}. number of edges {len(list(self.graph.edges))}"

if __name__ == "__main__":
    game = GameStruct()
    game.test_edge_data()
    print(game)