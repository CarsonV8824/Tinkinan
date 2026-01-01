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
        self.canvas.pack(expand=True, fill="none", side="left")
        self.hexagons = []
        self.pieces = []
        self.__get_pieces()
        self.__draw_board()
        self.on_canvas_click(None)
        
        #self.canvas.bind("<Button-1>", self.on_canvas_click)

    def __get_pieces(self) -> None:
        self.pieces_ref = {"sheep":"lime", "wood":"green", "brick":"brown", "wheat":"yellow", "ore":"gray", "desert":"tan"}
        
        for i in range(4):
            self.pieces.append(self.pieces_ref["sheep"])
            self.pieces.append(self.pieces_ref["wood"])
            self.pieces.append(self.pieces_ref["wheat"])
        for i in range(3):
            self.pieces.append(self.pieces_ref["brick"])
            self.pieces.append(self.pieces_ref["ore"])
        self.pieces.append(self.pieces_ref["desert"])

    def __draw_hexagon(self, x: float, y: float, size: float, fill_color: str) -> None:
        points = []
        for i in range(6):
            angle = math.radians(60 * i - 30)
            x_i = x + size * math.cos(angle)
            y_i = y + size * math.sin(angle)
            points.append((x_i, y_i))
        flat_points = [coord for point in points for coord in point]
        self.canvas.create_polygon(flat_points, outline='black', fill=fill_color, width=2)
        self.hexagons.append(flat_points)

    def draw_number_on_piece(self, piece_number: int, number: int | str) -> None:
        # Find the center of the hexagon for the given piece number
        hexagon_points = self.hexagons[piece_number - 1]
        x_coords = hexagon_points[0::2]
        y_coords = hexagon_points[1::2]
        center_x = sum(x_coords) / len(x_coords)
        center_y = sum(y_coords) / len(y_coords)
        
        # Draw the number at the center
        self.canvas.create_text(center_x, center_y, text=str(number), font=("Arial", 16), fill="black")

    def __draw_board(self) -> None:
        
        row_1_start_x = 325 - (50 * math.sqrt(3))
        row1_start_y = 325 - 150
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(1, color)

        number = self.game_struct.get_piece_dice_number(1)

        self.__draw_hexagon(row_1_start_x, row1_start_y, 50, color)
        self.draw_number_on_piece(1, number)

        row_2_start_x = 325
        row2_start_y = 325 - 150
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(2, color)

        number = self.game_struct.get_piece_dice_number(2)
        self.__draw_hexagon(row_2_start_x, row2_start_y, 50, color)
        self.draw_number_on_piece(2, number)

        row_3_start_x = 325 + (50 * math.sqrt(3))
        row3_start_y = 325 - (150)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(3, color)

        number = self.game_struct.get_piece_dice_number(3)
        self.__draw_hexagon(row_3_start_x, row3_start_y, 50, color)
        self.draw_number_on_piece(3, number)

        row_4_start_x = 325 - (1.5 * 50 * math.sqrt(3))
        row4_start_y = 325 - (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(4, color)

        number = self.game_struct.get_piece_dice_number(4)
        self.__draw_hexagon(row_4_start_x, row4_start_y, 50, color)
        self.draw_number_on_piece(4, number)

        row_5_start_x = 325 - (50 * 0.5 * math.sqrt(3))
        row5_start_y = 325 - (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(5, color)
        number = self.game_struct.get_piece_dice_number(5)
        self.__draw_hexagon(row_5_start_x, row5_start_y, 50, color)
        self.draw_number_on_piece(5, number)

        row_6_start_x = 325 + (50 * 0.5 * math.sqrt(3))
        row6_start_y = 325 - (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(6, color)
        number = self.game_struct.get_piece_dice_number(6)
        self.__draw_hexagon(row_6_start_x, row6_start_y, 50, color)
        self.draw_number_on_piece(6, number)

        row_7_start_x = 325 + (50 * 1.5 * math.sqrt(3))
        row7_start_y = 325 - (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(7, color)
        number = self.game_struct.get_piece_dice_number(7)
        self.__draw_hexagon(row_7_start_x, row7_start_y, 50, color)
        self.draw_number_on_piece(7, number)
        
        row_8_start_x = 325 - (2 * 50 * math.sqrt(3))
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(8, color)
        number = self.game_struct.get_piece_dice_number(8)
        self.__draw_hexagon(row_8_start_x, 325, 50, color)
        self.draw_number_on_piece(8, number)
        
        row_9_start_x = 325 - (50 * math.sqrt(3))
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(9, color)
        number = self.game_struct.get_piece_dice_number(9)
        self.__draw_hexagon(row_9_start_x, 325, 50, color)
        self.draw_number_on_piece(9, number)
        
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(10, color)
        self.__draw_hexagon(row_10_start_x := 325, 325, 50, color)
        number = self.game_struct.get_piece_dice_number(10)
        self.draw_number_on_piece(10, number)
        
        row_11_start_x = 325 + (50 * math.sqrt(3))
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(11, color)
        self.__draw_hexagon(row_11_start_x, 325, 50, color)
        number = self.game_struct.get_piece_dice_number(11)
        self.draw_number_on_piece(11, number)
        
        row_12_start_x = 325 + (2 * 50 * math.sqrt(3))
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(12, color)
        self.__draw_hexagon(row_12_start_x, 325, 50, color)
        number = self.game_struct.get_piece_dice_number(12)
        self.draw_number_on_piece(12, number)

        row_13_start_x = 325 - (1.5 * 50 * math.sqrt(3))
        row13_start_y = 325 + (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(13, color)
        self.__draw_hexagon(row_13_start_x, row13_start_y, 50, color)
        number = self.game_struct.get_piece_dice_number(13)
        self.draw_number_on_piece(13, number)

        row_14_start_x = 325 - (0.5 * 50 * math.sqrt(3))
        row14_start_y = 325 + (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(14, color)
        number = self.game_struct.get_piece_dice_number(14)
        self.__draw_hexagon(row_14_start_x, row14_start_y, 50, color)
        self.draw_number_on_piece(14, number)

        row_15_start_x = 325 + (0.5 * 50 * math.sqrt(3))
        row15_start_y = 325 + (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(15, color)
        number = self.game_struct.get_piece_dice_number(15)
        self.__draw_hexagon(row_15_start_x, row15_start_y, 50, color)
        self.draw_number_on_piece(15, number)

        row_16_start_x = 325 + (1.5 * 50 * math.sqrt(3))
        row16_start_y = 325 + (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(16, color)
        number = self.game_struct.get_piece_dice_number(16)
        self.__draw_hexagon(row_16_start_x, row16_start_y, 50, color)
        self.draw_number_on_piece(16, number)
        
        row_17_start_x = 325 - (50 * math.sqrt(3))
        row17_start_y = 325 + 150
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(17, color)
        number = self.game_struct.get_piece_dice_number(17)
        self.__draw_hexagon(row_17_start_x, row17_start_y, 50, color)
        self.draw_number_on_piece(17, number)

        row_18_start_x = 325
        row18_start_y = 325 + 150
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(18, color)
        number = self.game_struct.get_piece_dice_number(18)
        self.__draw_hexagon(row_18_start_x, row18_start_y, 50, color)
        self.draw_number_on_piece(18, number)

        row_19_start_x = 325 + (50 * math.sqrt(3))
        row19_start_y = 325 + 150
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(19, color)
        number = self.game_struct.get_piece_dice_number(19)
        self.__draw_hexagon(row_19_start_x, row19_start_y, 50, color)
        self.draw_number_on_piece(19, number)

    def __choose_radom_color_from_piece_list(self) -> str:
        return self.pieces.pop(random.randint(0, len(self.pieces)-1))
    
    def on_canvas_click(self, event):
        x, y = self.canvas.winfo_pointerxy()
        print(f"Canvas clicked at ({x}, {y})")
    


    