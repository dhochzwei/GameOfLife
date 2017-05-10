import game_of_life.universe as gol
from game_of_life.gui import GridFrame
from tkinter import *


class App(object):
    """shows the GUI """

    def __init__(self, master):
        frame = Frame(master)
        self.grid_size_entry = StringVar()
        menuframe = Frame(root)
        self.board = GridFrame(root)

        Label(menuframe, text="Grid Size").grid(row=0, sticky=W)
        Entry(menuframe, textvariable=self.grid_size_entry).grid(
            row=0, column=1, sticky=W)
        self.grid_size_entry.set("5")
        Button(menuframe, text="Init", command=self.button_init_callback).grid(
            row=0, column=2, sticky=W)
        Button(menuframe, text="Simulate Step", command=self.button_simulate_callback).grid(
            row=0, column=3, sticky=W)

        menuframe.pack(side="top", fill="x", expand="false", padx=4, pady=4,)
        self.board.pack(side="bottom", fill="both",
                        expand="true", padx=4, pady=4)

        self.universe = gol.Universe(5)
        self.universe.create()
        self.board.set_grid(self.universe.get_grid())
        self.board.redraw()

    def button_init_callback(self):
        entry_value = self.grid_size_entry.get()
        if entry_value.isdigit() and int(entry_value) > 0:            
            self.universe = gol.Universe(int(entry_value))
            self.universe.create()
            self.board.set_grid(self.universe.get_grid())
            self.board.redraw()

    def button_simulate_callback(self):
        self.universe.simulate_step()
        self.board.set_grid(self.universe.get_grid())
        self.board.redraw()


root = Tk()
app = App(root)
root.mainloop()
