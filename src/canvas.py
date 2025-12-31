from game_struct import GameStruct

from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk
import math
import random
from PIL import Image, ImageTk


class Canvas:

    def __init__(self, root: ThemedTk, game_struct: GameStruct):
        self.root = root
        self.game_struct = game_struct
        self.canvas = tk.Canvas(self.root, height=650, width=650)
        self.canvas.configure(bg='lightblue', border=2, relief='ridge', borderwidth=2)
        self.canvas.pack(expand=True, fill="none", anchor="center")
        self.hexagons = []
        self.pieces = []
        self.get_pieces()
        self.__draw_board()

    def get_pieces(self) -> None:
        self.pieces_ref = {"sheep":"lime", "wood":"green", "brick":"brown", "wheat":"yellow", "ore":"gray", "desert":"sienna"}
        
        for i in range(4):
            self.pieces.append(self.pieces_ref["sheep"])
            self.pieces.append(self.pieces_ref["wood"])
            self.pieces.append(self.pieces_ref["wheat"])
        for i in range(3):
            self.pieces.append(self.pieces_ref["brick"])
            self.pieces.append(self.pieces_ref["ore"])
        self.pieces.append(self.pieces_ref["desert"])

    def __draw_hexagon(self, x: float, y: float, size: float, fill_color: str):
        points = []
        for i in range(6):
            angle = math.radians(60 * i - 30)
            x_i = x + size * math.cos(angle)
            y_i = y + size * math.sin(angle)
            points.append((x_i, y_i))
        flat_points = [coord for point in points for coord in point]
        self.canvas.create_polygon(flat_points, outline='black', fill=fill_color, width=2)
        self.hexagons.append(flat_points)

    def __draw_board(self) -> None:
        
        row_1_start_x = 325 - (50 * math.sqrt(3))
        row1_start_y = 325 - 150
        self.__draw_hexagon(row_1_start_x, row1_start_y, 50, self.__choose_radom_color_from_piece_list())

        row_2_start_x = 325
        row2_start_y = 325 - 150
        self.__draw_hexagon(row_2_start_x, row2_start_y, 50, self.__choose_radom_color_from_piece_list())

        row_3_start_x = 325 + (50 * math.sqrt(3))
        row3_start_y = 325 - (150)
        self.__draw_hexagon(row_3_start_x, row3_start_y, 50, self.__choose_radom_color_from_piece_list())

        row_4_start_x = 325 - (1.5 * 50 * math.sqrt(3))
        row4_start_y = 325 - (50 * 1.5)
        self.__draw_hexagon(row_4_start_x, row4_start_y, 50, self.__choose_radom_color_from_piece_list())

        row_5_start_x = 325 - (50 * 0.5 * math.sqrt(3))
        row5_start_y = 325 - (50 * 1.5)
        self.__draw_hexagon(row_5_start_x, row5_start_y, 50, self.__choose_radom_color_from_piece_list())

        row_6_start_x = 325 + (50 * 0.5 * math.sqrt(3))
        row6_start_y = 325 - (50 * 1.5)
        self.__draw_hexagon(row_6_start_x, row6_start_y, 50, self.__choose_radom_color_from_piece_list())

        row_7_start_x = 325 + (50 * 1.5 * math.sqrt(3))
        row7_start_y = 325 - (50 * 1.5)
        self.__draw_hexagon(row_7_start_x, row7_start_y, 50, self.__choose_radom_color_from_piece_list())
        
        row_8_start_x = 325 - (2 * 50 * math.sqrt(3))
        self.__draw_hexagon(row_8_start_x, 325, 50, self.__choose_radom_color_from_piece_list())
        
        row_9_start_x = 325 - (50 * math.sqrt(3))
        self.__draw_hexagon(row_9_start_x, 325, 50, self.__choose_radom_color_from_piece_list())
        
        self.__draw_hexagon(row_10_start_x := 325, 325, 50, self.__choose_radom_color_from_piece_list())
        
        row_11_start_x = 325 + (50 * math.sqrt(3))
        self.__draw_hexagon(row_11_start_x, 325, 50, self.__choose_radom_color_from_piece_list())
        
        row_12_start_x = 325 + (2 * 50 * math.sqrt(3))
        self.__draw_hexagon(row_12_start_x, 325, 50, self.__choose_radom_color_from_piece_list())

        row_13_start_x = 325 - (1.5 * 50 * math.sqrt(3))
        row13_start_y = 325 + (50 * 1.5)
        self.__draw_hexagon(row_13_start_x, row13_start_y, 50, self.__choose_radom_color_from_piece_list())

        row_14_start_x = 325 - (0.5 * 50 * math.sqrt(3))
        row14_start_y = 325 + (50 * 1.5)
        self.__draw_hexagon(row_14_start_x, row14_start_y, 50, self.__choose_radom_color_from_piece_list())

        row_15_start_x = 325 + (0.5 * 50 * math.sqrt(3))
        row15_start_y = 325 + (50 * 1.5)
        self.__draw_hexagon(row_15_start_x, row15_start_y, 50, self.__choose_radom_color_from_piece_list())

        row_16_start_x = 325 + (1.5 * 50 * math.sqrt(3))
        row16_start_y = 325 + (50 * 1.5)
        self.__draw_hexagon(row_16_start_x, row16_start_y, 50, self.__choose_radom_color_from_piece_list())
        
        row_17_start_x = 325 - (50 * math.sqrt(3))
        row17_start_y = 325 + 150
        self.__draw_hexagon(row_17_start_x, row17_start_y, 50, self.__choose_radom_color_from_piece_list())

        row_18_start_x = 325
        row18_start_y = 325 + 150
        self.__draw_hexagon(row_18_start_x, row18_start_y, 50, self.__choose_radom_color_from_piece_list())

        row_19_start_x = 325 + (50 * math.sqrt(3))
        row19_start_y = 325 + 150
        self.__draw_hexagon(row_19_start_x, row19_start_y, 50, self.__choose_radom_color_from_piece_list())

    def __choose_radom_color_from_piece_list(self) -> str:
        return self.pieces.pop(random.randint(0, len(self.pieces)-1))


    