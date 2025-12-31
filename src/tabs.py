from tkinter import ttk  
from ttkthemes import ThemedTk
import tkinter as tk

class Tabs:

    def __init__(self, root:ThemedTk):
        self.root = root

    def tabs(self):
        tab = ttk.Notebook(self.root)
        tab.pack(expand=True, fill="both")
        return tab
    
    def dice_tab(self, notebook:ttk.Notebook):

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

        return dice_tab

    def trade_tab(self, notebook:ttk.Notebook):

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

        return trade_tab

    def biuld_tab(self, notebook:ttk.Notebook):
        
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
            rules_text = tk.Text(rules_toplevel, wrap="word")
            rules_text.pack(expand=True, fill="both")
            rules_text.insert("1.0", "Here are the rules of the game...\n\n1. Rule one...\n2. Rule two...\n3. Rule three...\n\nEnjoy playing Catan!")
            rules_text.config(state="disabled")
            
        rule_button  = ttk.Button(frame, text="Show Rules", command=show_rules)
        rule_button.pack(pady=10)

        return rules_tab

