import tkinter as tk
import numpy as np
from game_of_life.universe import Universe


class GridFrame(tk.Frame):
    def __init__(self, parent, grid_size=5, size=32, live_color="black", dead_color="white"):
        self.uni = Universe(grid_size)
        self.uni.create()
        self.grid = np.zeros((grid_size, grid_size))
        self.grid[2, 1] = 1
        self.rows = grid_size
        self.columns = grid_size
        self.size = size
        self.live_color = live_color
        self.dead_color = dead_color
        self.parent = parent

        canvas_width = grid_size * size
        canvas_height = grid_size * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="white")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        self.redraw()

    def redraw(self):

        self.canvas.delete("square")
        self.grid = self.uni.get_grid()

        for row in range(self.rows):
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                if self.grid[row, col] == 1:
                    color = self.live_color
                else:
                    color = self.dead_color
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, outline="black", fill=color, tags="square")
        self.uni.simulate_step()
        self.parent.after(50, self.redraw)

    def set_grid(self, grid):
        self.grid = grid
