from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk
from canvas import Canvas
from db import Database
from game_loop import GameLoop

class Player:

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        self.resources = {
            "lime": 0,
            "green": 0,
            "brown": 0,
            "yellow": 0,
            "gray": 0,
            "victory_points":2,
        }
        self.settlements = []
        self.cities = []
        self.roads = []

    def add_resource(self, resource: str, amount: int):
        if resource in self.resources:
            self.resources[resource] += amount
        else:
            raise ValueError(f"Resource {resource} not recognized.")
        
    def remove_resource(self, resource: str, amount: int):
        if resource in self.resources:
            if self.resources[resource] >= amount:
                self.resources[resource] -= amount
            else:
                raise ValueError(f"Not enough {resource} to remove.")
        else:
            raise ValueError(f"Resource {resource} not recognized.")
        
    def get_resource_count(self, resource: str) -> int:
        if resource in self.resources:
            return self.resources[resource]
        else:
            raise ValueError(f"Resource {resource} not recognized.")
        
    def add_settlement(self, settlement):
        self.settlements.append(settlement)

    def add_city(self, city):
        self.settlements.remove(city)
        self.cities.append(city)

    def add_road(self, road):
        self.roads.append(road)

    def add_victory_point(self, points: int):
        self.resources["victory_points"] += points

        
    