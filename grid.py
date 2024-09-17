import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D
import numpy as np

class Grid:
    def __init__(self):
        self.grid = np.full((3, 3), ' ')
        self.fig, self.ax = plt.subplots(1, 1, figsize=(8, 8))
        self.setup_grid()
        self.symbols = []

    def setup_grid(self):
        self.ax.plot([1/3, 1/3], [0, 1], 'k')
        self.ax.plot([2/3, 2/3], [0, 1], 'k')
        self.ax.plot([0, 1], [1/3, 1/3], 'k')
        self.ax.plot([0, 1], [2/3, 2/3], 'k')
        self.ax.axis("equal")
        self.ax.set_xlim((0, 1))
        self.ax.set_ylim((0, 1))
        self.ax.set_xticks([])
        self.ax.set_yticks([])

    def place_mark(self, row, col, symbol):
        if self.grid[row, col] == ' ':
            self.grid[row, col] = symbol
            position = (col/3 + 1/6, 1 - (row/3 + 1/6))
            if symbol == 'O':
                self.draw_circle(position)
            else:
                self.draw_x(position)
            return True
        return False

    def draw_circle(self, position):
        circle = Circle(position, 0.1, color='b', fill=False, linewidth=2)
        self.ax.add_artist(circle)
        self.symbols.append(circle)

    def draw_x(self, position):
        x, y = position
        cross1 = Line2D([x - 0.1, x + 0.1], [y - 0.1, y + 0.1], color='r', linewidth=3)
        cross2 = Line2D([x - 0.1, x + 0.1], [y + 0.1, y - 0.1], color='r', linewidth=3)
        self.ax.add_artist(cross1)
        self.ax.add_artist(cross2)
        self.symbols.append(cross1)
        self.symbols.append(cross2)

    def display(self):
        plt.draw()
        plt.pause(0.1)

    def check_victory(self, symbol):
        return (np.any(np.all(self.grid == symbol, axis=1)) or
                np.any(np.all(self.grid == symbol, axis=0)) or
                np.all(np.diag(self.grid) == symbol) or
                np.all(np.diag(np.fliplr(self.grid)) == symbol))

    def is_full(self):
        return np.all(self.grid != ' ')