import time
from cell import Cell
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self.win = win
        self._cells = []
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.x1 = x1
        self.y1 = y1
        self._create_cells()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x =self.x1 + (self.cell_size_x * i)
        y = self.y1 + (self.cell_size_y * j)
        self._cells[i][j].draw(x, x+self.cell_size_x,
                               y, y+self.cell_size_y)
        self._animate()

    def _create_cells(self):
        self._cells = [[Cell(self.win) for _ in range(self.num_rows)] for _ in range(self.num_cols) ]
        for i,col in enumerate(self._cells):
            for j,cell in enumerate(col):
                self._draw_cell(i,j)

    