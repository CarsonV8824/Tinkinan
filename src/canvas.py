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

        self.coords = ()

        self.current_player = None #to track current player for placement

        self.settlement_on = False

        self.road_on = False
        
        self.city_on = False

        #look at Game_Board.png to see how the corner coords are mapped to piece numbers
        self.corner_coords = {
            1: (238.39745962155615, 125.0),
            2: (281.6987298107781, 150.0),
            3: (325.0, 125.0),
            4: (368.30127018922195, 150.0),
            5: (411.60254037844385, 125.0),
            6: (454.9038105676658, 150.0),
            7: (454.9038105676658, 200.0),
            8: (498.20508075688775, 225.0),
            9: (498.20508075688775, 275.0),
            10: (541.5063509461096, 300.0),
            11: (541.5063509461096, 350.0),
            12: (498.2050807568877, 375.0),
            13: (498.20508075688775, 425.0),
            14: (454.9038105676658, 450.0),
            15: (454.9038105676658, 500.0),
            16: (411.60254037844385, 525.0),
            17: (368.30127018922195, 500.0),
            18: (325.0, 525.0),
            19: (281.6987298107781, 500.0),
            20: (238.39745962155615, 525.0),
            21: (195.0961894323342, 500.0),
            22: (195.0961894323342, 450.0),
            23: (151.79491924311225, 425.0),
            24: (151.79491924311228, 375.0),
            25: (108.49364905389034, 350.0),
            26: (108.49364905389035, 300.0),
            27: (151.79491924311225, 275.0),
            28: (151.79491924311228, 225.0),
            29: (195.0961894323342, 200.0),
            30: (195.09618943233423, 150.0),
            31: (281.6987298107781, 200.0),
            32: (325.0, 225.0),
            33: (368.30127018922195, 200.0),
            34: (411.60254037844385, 225.0),
            35: (411.6025403784439, 275.0),
            36: (454.9038105676658, 300.0),
            37: (454.9038105676658, 350.0),
            38: (411.60254037844385, 375.0),
            39: (411.6025403784439, 425.0),
            40: (368.30127018922195, 450.0),
            41: (325.0, 425.0),
            42: (281.69872981077805, 450.0),
            43: (238.39745962155615, 425.0),
            44: (238.39745962155615, 375.0),
            45: (195.0961894323342, 350.0),
            46: (195.0961894323342, 300.0),
            47: (238.39745962155615, 275.0),
            48: (238.39745962155615, 225.0),
            49: (325.0, 275.0),
            50: (368.30127018922195, 300.0),
            51: (368.30127018922195, 350.0),
            52: (325.0, 375.0),
            53: (281.6987298107781, 350.0),
            54: (281.69872981077805, 300.0)
        }

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
        
        #--- Row 1 ---

        row_1_start_x = 325 - (50 * math.sqrt(3))
        row1_start_y = 325 - 150
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(1, color)

        number = self.game_struct.get_piece_dice_number(1)

        self.__draw_hexagon(row_1_start_x, row1_start_y, 50, color)
        self.draw_number_on_piece(1, number)

        #--- Row 2 ---

        row_2_start_x = 325
        row2_start_y = 325 - 150
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(2, color)

        number = self.game_struct.get_piece_dice_number(2)
        self.__draw_hexagon(row_2_start_x, row2_start_y, 50, color)
        self.draw_number_on_piece(2, number)

        #--- Row 3 ---

        row_3_start_x = 325 + (50 * math.sqrt(3))
        row3_start_y = 325 - (150)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(3, color)

        number = self.game_struct.get_piece_dice_number(3)
        self.__draw_hexagon(row_3_start_x, row3_start_y, 50, color)
        self.draw_number_on_piece(3, number)

        #--- Row 4 ---

        row_7_start_x = 325 + (50 * 1.5 * math.sqrt(3))
        row7_start_y = 325 - (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(4, color)
        number = self.game_struct.get_piece_dice_number(4)
        self.__draw_hexagon(row_7_start_x, row7_start_y, 50, color)
        self.draw_number_on_piece(4, number)

        #-- Row 5 ---

        row_12_start_x = 325 + (2 * 50 * math.sqrt(3))
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(5, color)
        self.__draw_hexagon(row_12_start_x, 325, 50, color)
        number = self.game_struct.get_piece_dice_number(5)
        self.draw_number_on_piece(5, number)

        #-- Row 6 ---

        row_16_start_x = 325 + (1.5 * 50 * math.sqrt(3))
        row16_start_y = 325 + (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(6, color)
        number = self.game_struct.get_piece_dice_number(6)
        self.__draw_hexagon(row_16_start_x, row16_start_y, 50, color)
        self.draw_number_on_piece(6, number)

        #-- Row 7 ---

        row_19_start_x = 325 + (50 * math.sqrt(3))
        row19_start_y = 325 + 150
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(7, color)
        number = self.game_struct.get_piece_dice_number(7)
        self.__draw_hexagon(row_19_start_x, row19_start_y, 50, color)
        self.draw_number_on_piece(7, number)
        
        #--- Row 8 ---

        row_18_start_x = 325
        row18_start_y = 325 + 150
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(8, color)
        number = self.game_struct.get_piece_dice_number(8)
        self.__draw_hexagon(row_18_start_x, row18_start_y, 50, color)
        self.draw_number_on_piece(8, number)
        
        #--- Row 9 ---

        row_17_start_x = 325 - (50 * math.sqrt(3))
        row17_start_y = 325 + 150
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(9, color)
        number = self.game_struct.get_piece_dice_number(9)
        self.__draw_hexagon(row_17_start_x, row17_start_y, 50, color)
        self.draw_number_on_piece(9, number)
        
        #--- Row 10 ---

        row_13_start_x = 325 - (1.5 * 50 * math.sqrt(3))
        row13_start_y = 325 + (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(10, color)
        self.__draw_hexagon(row_13_start_x, row13_start_y, 50, color)
        number = self.game_struct.get_piece_dice_number(10)
        self.draw_number_on_piece(10, number)
        
        #--- Row 11 ---

        

        row_8_start_x = 325 - (2 * 50 * math.sqrt(3))
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(11, color)
        number = self.game_struct.get_piece_dice_number(11)
        self.__draw_hexagon(row_8_start_x, 325, 50, color)
        self.draw_number_on_piece(11, number)
        
        #--- Row 12 ---

        row_4_start_x = 325 - (1.5 * 50 * math.sqrt(3))
        row4_start_y = 325 - (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(12, color)

        number = self.game_struct.get_piece_dice_number(12)
        self.__draw_hexagon(row_4_start_x, row4_start_y, 50, color)
        self.draw_number_on_piece(12, number)
        #--- Row 13 ---

        row_5_start_x = 325 - (50 * 0.5 * math.sqrt(3))
        row5_start_y = 325 - (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(13, color)
        number = self.game_struct.get_piece_dice_number(13)
        self.__draw_hexagon(row_5_start_x, row5_start_y, 50, color)
        self.draw_number_on_piece(13, number)

        #--- Row 14 ---

        row_6_start_x = 325 + (50 * 0.5 * math.sqrt(3))
        row6_start_y = 325 - (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(14, color)
        number = self.game_struct.get_piece_dice_number(14)
        self.__draw_hexagon(row_6_start_x, row6_start_y, 50, color)
        self.draw_number_on_piece(14, number)

        #--- Row 15 ---

        row_11_start_x = 325 + (50 * math.sqrt(3))
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(15, color)
        self.__draw_hexagon(row_11_start_x, 325, 50, color)
        number = self.game_struct.get_piece_dice_number(15)
        self.draw_number_on_piece(15, number)

        #--- Row 16 ---

        row_15_start_x = 325 + (0.5 * 50 * math.sqrt(3))
        row15_start_y = 325 + (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(16, color)
        number = self.game_struct.get_piece_dice_number(16)
        self.__draw_hexagon(row_15_start_x, row15_start_y, 50, color)
        self.draw_number_on_piece(16, number)
        
        #--- Row 17 ---

        row_14_start_x = 325 - (0.5 * 50 * math.sqrt(3))
        row14_start_y = 325 + (50 * 1.5)
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(17, color)
        number = self.game_struct.get_piece_dice_number(17)
        self.__draw_hexagon(row_14_start_x, row14_start_y, 50, color)
        self.draw_number_on_piece(17, number)

        #--- Row 18 ---

        row_9_start_x = 325 - (50 * math.sqrt(3))
        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(18, color)
        number = self.game_struct.get_piece_dice_number(18)
        self.__draw_hexagon(row_9_start_x, 325, 50, color)
        self.draw_number_on_piece(18, number)

        #--- Row 19 ---

        color = self.__choose_radom_color_from_piece_list()
        self.game_struct.add_image_color_to_piece(19, color)
        self.__draw_hexagon(row_10_start_x := 325, 325, 50, color)
        number = self.game_struct.get_piece_dice_number(19)
        self.draw_number_on_piece(19, number)

    def __choose_radom_color_from_piece_list(self) -> str:
        return self.pieces.pop(random.randint(0, len(self.pieces)-1))

    def is_corner_hit(self, event, tolerance=10):
        cx, cy = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        for idx, flat_points in enumerate(self.hexagons, start=1):
            for x_i, y_i in zip(flat_points[0::2], flat_points[1::2]):
                dx, dy = cx - x_i, cy - y_i
                if (dx*dx + dy*dy) ** 0.5 <= tolerance:
                    return idx, (x_i, y_i)  # piece number, corner coords
        return None, None
    
    def is_edge_hit(self, event, tolerance=10):
        cx, cy = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        for idx, flat_points in enumerate(self.hexagons, start=1):
            for i in range(6):
                x1, y1 = flat_points[2*i], flat_points[2*i + 1]
                x2, y2 = flat_points[2*((i + 1) % 6)], flat_points[2*((i + 1) % 6) + 1]
                
                # Calculate distance from point to line segment
                A = cx - x1
                B = cy - y1
                C = x2 - x1
                D = y2 - y1

                dot = A * C + B * D
                len_sq = C * C + D * D
                param = dot / len_sq if len_sq != 0 else -1

                if param < 0:
                    xx, yy = x1, y1
                elif param > 1:
                    xx, yy = x2, y2
                else:
                    xx = x1 + param * C
                    yy = y1 + param * D

                dx = cx - xx
                dy = cy - yy
                if (dx*dx + dy*dy) ** 0.5 <= tolerance:
                    return idx, ((x1, y1), (x2, y2))   # piece number, edge coords of what houses inbetween
        return None, None
    
    def get_corner_num(self, corner, tolerance=0.01):
        """Find corner number by coordinate with tolerance for floating-point errors"""
        for key, (x, y) in self.corner_coords.items():
            try:
                if abs(x - corner[0]) < tolerance and abs(y - corner[1]) < tolerance:
                    return key
            except TypeError as e:
                print(str(e) + " in get_corner_num")
        return None
    
    def draw_road(self, x1: float, y1: float, x2: float, y2: float, color: str) -> None:
        self.canvas.create_line(x1, y1, x2, y2, fill=color, width=6)
    
    def draw_settlement(self, x: float, y: float, color: str) -> None:
        size = 10
        points = [
            (x - size, y),
            (x, y - size),
            (x + size, y),
            (x + size, y + size),
            (x - size, y + size)
        ]
        flat_points = [coord for point in points for coord in point]
        self.canvas.create_polygon(flat_points, outline='black', fill=color, width=2)

    def settlement_init(self, current_player):
        self.placement_complete = False

        def on_canvas_click(event):
            if self.placement_complete:
                return  # Ignore clicks if placement is complete

            hit_piece, corner = self.is_corner_hit(event)

            corner_num = self.get_corner_num(corner)
            if hit_piece:
                # Here you would add logic to place settlement/road
                
                check = self.game_struct.check_house_occupancy_empty(corner_num)
                if check:
                    x_cord = corner[0]
                    y_cord = corner[1]
                    self.draw_settlement(x_cord, y_cord, current_player.color)
                    self.game_struct.add_player_to_house(corner_num, current_player.name, "House")
                    print(f"{current_player.name} clicked on piece {hit_piece} at {corner}")
                    self.placement_complete = True  # Mark placement as complete
                
                elif not check:
                    print(f"Corner {corner_num} is already occupied.")
                    # return

            else:
                print("No corner hit")

        self.canvas.bind("<Button-1>", on_canvas_click)

        # Wait until placement is complete
        while not self.placement_complete:
            self.root.update()

    def road_init(self, current_player):
        self.placement_complete = False

        def on_canvas_click(event):
            if self.placement_complete:
                return

            hit_piece, edge_coords = self.is_edge_hit(event)
            
            if edge_coords is None:
                print("No edge hit")
                return
            
            house1_num, house2_num = edge_coords
            house1_corner_num = self.get_corner_num(house1_num)
            house2_corner_num = self.get_corner_num(house2_num)
            
            if hit_piece:
                print(f"{current_player.name} clicked on edge {hit_piece} at {edge_coords}")
                road_check = self.game_struct.check_road_occupancy(house1_corner_num, house2_corner_num)
                
                # Check if player owns a settlement at either endpoint
                has_settlement_endpoint = (
                    self.game_struct.check_house_owner(house1_corner_num, current_player.name) or
                    self.game_struct.check_house_owner(house2_corner_num, current_player.name)
                )
                
                if road_check and has_settlement_endpoint:
                    x1, y1 = house1_num
                    x2, y2 = house2_num
                    self.draw_road(x1, y1, x2, y2, current_player.color)
                    self.game_struct.add_player_to_road(house1_corner_num, house2_corner_num, current_player.name)
                    self.placement_complete = True
                else:
                    if not has_settlement_endpoint:
                        print(f"You must have a settlement at one end of this road.")

        self.canvas.bind("<Button-1>", on_canvas_click)

        while not self.placement_complete:
            self.root.update()

    def get_player(self, player):
        self.current_player = player
        print(f"Current player set to {player.name}")

    def settlement_mode(self, event):
        self.canvas.bind("<s>", lambda e: (setattr(self, 'settlement_on', True), 
                        setattr(self, 'road_on', False), 
                        setattr(self, 'city_on', False)))

    def city_mode(self, event):
        self.canvas.bind("<c>", lambda e: (setattr(self, 'city_on', True),
                        setattr(self, 'settlement_on', False), 
                        setattr(self, 'road_on', False)))
        
    def road_mode(self, event):
        self.canvas.bind("<r>", lambda e: (setattr(self, 'road_on', True),
                        setattr(self, 'settlement_on', False), 
                        setattr(self, 'city_on', False)))

    def on_canvas_click_game_loop(self, event): #make this method make the player able to buy settlements, roads, and cities
        
        print(self.current_player.name + " clicked the canvas")
        
        hit_piece, corner = self.is_corner_hit(event)
        hit_piece_edge, edge_coords = self.is_edge_hit(event)
        if hit_piece:
            print(f"Clicked on piece {hit_piece} at {corner}!")
        elif hit_piece_edge:
            print(f"Clicked on edge {hit_piece_edge} at {edge_coords}!")
        else:
            print("No corner hit")

    
        
    

    

    
    
    

        
    


    