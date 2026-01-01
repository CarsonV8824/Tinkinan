from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk
from canvas import Canvas
from game_struct import GameStruct
from db import Database
from game_struct import GameStruct
from game_loop import GameLoop

class Player:

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        self.resources = {
            "sheep": 0,
            "wood": 0,
            "brick": 0,
            "wheat": 0,
            "ore": 0
        }
        self.settlements = []
        self.cities = []
        self.roads = []