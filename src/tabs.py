from logging import root
from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk
from player import Player
from game_loop import GameLoop

class Tabs:

    def __init__(self, root:ThemedTk):
        self.root = root
        self.biuld_option = None
        
        self.first_trade_player_text = None
        self.second_trade_player_text = None
        
        self.first_trade_player = None
        self.second_trade_player = None
        
        self.first_player_items:ttk.Treeview = None
        self.second_player_items:ttk.Treeview = None

    def tabs(self):
        tab = ttk.Notebook(self.root)
        tab.pack(expand=True, fill="both")
        return tab
    
    def dice_tab(self, notebook:ttk.Notebook, game_loop: GameLoop, players:list):

        dice_tab = ttk.Frame(notebook)
        notebook.add(dice_tab, text="dice")
        
        #===Scrollbar======================================================================================

        canvas = tk.Canvas(dice_tab)
        scrollbar = ttk.Scrollbar(dice_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        frame = ttk.Frame(scrollable_frame)
        frame.pack(expand=True, fill="both")

        #=====================================================================================

        dice_button = ttk.Button(frame, text="Roll Dice", command=lambda: game_loop.game_turn(dice_button, player_turn_info, players=players, first_dice_label=first_dice, second_dice_label=second_dice, total_of_dice_label=total_of_dice, update_player_stats_tab=lambda: self.update_player_stats(players)))

        dice_button.pack(pady=20)

        player_turn_info = ttk.Label(frame, text=f"{players[game_loop.player_index].name}'s Turn")
        player_turn_info.pack(pady=10)

        first_dice = ttk.Label(frame, text="First Dice Roll: ")
        first_dice.pack()

        second_dice = ttk.Label(frame, text="Second Dice Roll: ")
        second_dice.pack()

        total_of_dice = ttk.Label(frame, text="Total of Dice: ")
        total_of_dice.pack()
        
        return dice_tab
    
    def player_stats_tab(self, notebook:ttk.Notebook, players:list):
        player_stats_tab = ttk.Frame(notebook)
        notebook.add(player_stats_tab, text="player stats")
        
        #===Scrollbar======================================================================================

        canvas = tk.Canvas(player_stats_tab)
        scrollbar = ttk.Scrollbar(player_stats_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        frame = ttk.Frame(scrollable_frame)
        frame.pack(expand=True, fill="both")

        #=====================================================================================

        self.player_stat_vars = {}
        for player in players:
            player:Player = player
            player_frame = ttk.LabelFrame(frame, text=player.name, padding=10)
            player_frame.pack(fill="x", padx=10, pady=5)

            color_var = tk.StringVar(self.root, value=f"Color: {player.color}")
            ttk.Label(player_frame, textvariable=color_var).pack(anchor="w")

            stats_label = ttk.Label(player_frame, text="Stats:")
            stats_label.pack(anchor="w")

            resource_vars = {}
            for resource, amount in player.resources.items():
                res_var = tk.StringVar(self.root, value=f"  {resource}: {amount}")
                resource_vars[resource] = res_var
                ttk.Label(player_frame, textvariable=res_var).pack(anchor="w")

            self.player_stat_vars[player.name] = {"color": color_var, "resources": resource_vars}

        return player_stats_tab
    
    def update_player_stats(self, players: list):
        for player in players:
            player:Player = player
            vars_map = self.player_stat_vars.get(player.name)
            if not vars_map:
                continue  
            vars_map["color"].set(f"Color: {player.color}")
            for resource, amount in player.resources.items():
                res_var = vars_map["resources"].get(resource)
                if res_var:
                    res_var.set(f"  {resource}: {amount}")

    def trade_tab(self, notebook:ttk.Notebook, players:list):

        trade_tab = ttk.Frame(notebook)
        notebook.add(trade_tab, text="trade")
        
        #===Scrollbar======================================================================================

        canvas = tk.Canvas(trade_tab)
        scrollbar = ttk.Scrollbar(trade_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        frame = ttk.Frame(scrollable_frame)
        frame.pack(expand=True, fill="both")

        #=====================================================================================

        first_trade_player = ttk.Combobox(frame, values=[player.name for player in players], state="readonly")
        first_trade_player.pack(padx=10, pady=10)

        second_trade_player = ttk.Combobox(frame, values=[player.name for player in players], state="readonly")
        second_trade_player.pack(padx=10, pady=10)

        first_player = first_trade_player.get()
        second_player = second_trade_player.get()

        def on_select_first(event):
            print("Selected:", first_trade_player.get())
            self.first_trade_player = first_trade_player.get()
            
            try:
                self.first_player_items.destroy()
                self.first_trade_player_text.destroy()
            except Exception:
                pass
            
            self.first_trade_player_text = ttk.Label(frame, text=f"{self.first_trade_player}'s Resources:")
            self.first_trade_player_text.pack(padx=10, pady=10)
            self.first_player_items = ttk.Treeview(frame, selectmode="extended", show="tree")
            self.first_player_items.pack(padx=10, pady=10)
            try:
                self.first_player_items.delete(0, tk.END)
            except Exception:
                pass
            for resource, amount in next(player for player in players if player.name == self.first_trade_player).resources.items():
                for _ in range(amount):
                    if resource != "victory_points":
                        
                        try:
                            self.first_player_items.insert('', 'end', text=resource)
                        except Exception as e:
                            print(e)
            
            item_count = len(self.first_player_items.get_children())
            self.first_player_items.config(height=item_count if item_count > 0 else 1)
        first_trade_player.bind("<<ComboboxSelected>>", on_select_first)

        def on_select_second(event):
            print("Selected:", second_trade_player.get())
            self.second_trade_player = second_trade_player.get()
            try:
                self.second_player_items.destroy()
                self.second_trade_player_text.destroy()
            except Exception:
                pass
            self.second_trade_player_text = ttk.Label(frame, text=f"{self.second_trade_player}'s Resources:")
            self.second_trade_player_text.pack(padx=10, pady=10)
            self.second_player_items = ttk.Treeview(frame, selectmode="extended", show="tree")
            self.second_player_items.pack(padx=10, pady=10)
            try:
                self.second_player_items.delete(0, tk.END)
            except Exception:
                pass
            for resource, amount in next(player for player in players if player.name == self.second_trade_player).resources.items():
                for _ in range(amount):
                    if resource != "victory_points":
                        try:
                            self.second_player_items.insert('', 'end', text=resource)
                        except Exception as e:
                            print(e)
            self.second_player_items.config(height=len(self.second_player_items.get_children()) if len(self.second_player_items.get_children()) > 0 else 1)
        
        second_trade_player.bind("<<ComboboxSelected>>", on_select_second)

        def get_trade_selections():
            if not self.first_trade_player or not self.second_trade_player:
                return

            first_selected = list(self.first_player_items.selection())  
            second_selected = list(self.second_player_items.selection()) 
            
            first_items = []
            second_items = []
            
            # Get details from selections
            for item_id in first_selected:
                item_data = self.first_player_items.item(item_id)
                first_items.append(item_data['text'])
            
            for item_id in second_selected:
                item_data = self.second_player_items.item(item_id)
                second_items.append(item_data['text'])
            
            # Update player resources
            for player in players:
                if player.name == self.first_trade_player:
                    for resource in first_items:
                        player.remove_resource(resource, 1)
                    for resource in second_items:
                        player.add_resource(resource, 1)
                elif player.name == self.second_trade_player:
                    for resource in second_items:
                        player.remove_resource(resource, 1)
                    for resource in first_items:
                        player.add_resource(resource, 1)
            
            # Delete items AFTER updating all player resources
            for item_id in first_selected:
                self.first_player_items.delete(item_id)
            
            for item_id in second_selected:
                self.second_player_items.delete(item_id)
            
            # Add new items for trades received
            for resource in second_items:
                self.first_player_items.insert('', 'end', text=resource)
            
            for resource in first_items:
                self.second_player_items.insert('', 'end', text=resource)
            
            # Update heights
            self.first_player_items.config(height=len(self.first_player_items.get_children()) or 1)
            self.second_player_items.config(height=len(self.second_player_items.get_children()) or 1)

        trade_confirm_button = ttk.Button(
            frame, 
            text="Confirm Trade", 
            command=lambda: get_trade_selections()
        )
        trade_confirm_button.pack(pady=10)

        return trade_tab

    def build_tab(self, notebook:ttk.Notebook):
        
        biuld_tab = ttk.Frame(notebook)
        notebook.add(biuld_tab, text="biuld")
        
        #===Scrollbar======================================================================================

        canvas = tk.Canvas(biuld_tab)
        scrollbar = ttk.Scrollbar(biuld_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        frame = ttk.Frame(scrollable_frame)
        frame.pack(expand=True, fill="both")

        #=====================================================================================

        road = ttk.Label(frame, text="Press r to build a road")
        road.pack(padx=10, pady=10)

        settlement = ttk.Label(frame, text="Press s to build a settlement")
        settlement.pack(padx=10, pady=10)

        city = ttk.Label(frame, text="Press c to build a city")
        city.pack(padx=10, pady=10)

        """combo = ttk.Combobox(frame, values=["road", "settlement", "city"], state="readonly")
        combo.current(0)  
        combo.pack(padx=10, pady=10)

        def on_select(event):
            print("Selected:", combo.get())
            self.biuld_option = combo.get()
        combo.bind("<<ComboboxSelected>>", on_select)"""
        
        return biuld_tab

    def rules_tab(self, notebook:ttk.Notebook):
        
        rules_tab = ttk.Frame(notebook)
        notebook.add(rules_tab, text="rules")
        
        #===Scrollbar======================================================================================

        canvas = tk.Canvas(rules_tab)
        scrollbar = ttk.Scrollbar(rules_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        frame = ttk.Frame(scrollable_frame)
        frame.pack(expand=True, fill="both")

        #=====================================================================================

        def show_rules():
            rules_toplevel = tk.Toplevel(rules_tab)
            rules_toplevel.title("Game Rules")
            rules_toplevel.geometry("600x400")
            
            
            frame = ttk.Frame(rules_toplevel)
            frame.pack(expand=True, fill="both", padx=10, pady=10)
            
           
            scrollbar = ttk.Scrollbar(frame, orient="vertical")
            scrollbar.pack(side="right", fill="y")
            
            
            rules_text = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set)
            rules_text.pack(side="left", expand=True, fill="both")
            
            
            scrollbar.config(command=rules_text.yview)
            
            with open("config/rules.txt", "r") as file:
                rules_content = file.read()
            rules_text.insert("1.0", rules_content)
            rules_text.config(state="disabled")
            
        rule_button  = ttk.Button(frame, text="Show Rules", command=show_rules)
        rule_button.pack(pady=10)

        return rules_tab

