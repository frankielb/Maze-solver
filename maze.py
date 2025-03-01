import time
from cell import Cell
import random
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
        seed = None
    ):
        self.win = win
        self._cells = []
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.x1 = x1
        self.y1 = y1
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        self.solve()

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

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            ijs = []
            if i>0 and self._cells[i-1][j].visited == False:
                ijs.append(['l',i-1,j])
            if j>0 and self._cells[i][j-1].visited == False:
                ijs.append(['u',i,j-1])
            if i<len(self._cells)-1 and self._cells[i+1][j].visited == False:
                ijs.append(['r',i+1,j])
            if j<len(self._cells[0])-1 and self._cells[i][j+1].visited == False:
                ijs.append(['d',i,j+1])
            if len(ijs) == 0:
                self._draw_cell(i,j)
                return
            else:
                direction = random.choice(ijs)
                if direction[0] == 'l':
                    self._cells[i][j].has_left_wall = False
                    self._draw_cell(i,j)
                    self._cells[i-1][j].has_right_wall = False
                    self._draw_cell(i-1,j)
                if direction[0] == 'r':
                    self._cells[i][j].has_right_wall = False
                    self._draw_cell(i,j)
                    self._cells[i+1][j].has_left_wall = False
                    self._draw_cell(i+1,j)
                if direction[0] == 'u':
                    self._cells[i][j].has_top_wall = False
                    self._draw_cell(i,j)
                    self._cells[i][j-1].has_bottom_wall = False
                    self._draw_cell(i,j-1)
                if direction[0] == 'd':
                    self._cells[i][j].has_bottom_wall = False
                    self._draw_cell(i,j)
                    self._cells[i][j+1].has_top_wall = False
                    self._draw_cell(i,j+1)
                self._break_walls_r(direction[1],direction[2])
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True

        if i>0 and self._cells[i-1][j].visited == False and self._cells[i-1][j].has_right_wall == False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j],True)

        if j>0 and self._cells[i][j-1].visited == False and self._cells[i][j-1].has_bottom_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1],True)

        if i<len(self._cells)-1 and self._cells[i+1][j].visited == False and self._cells[i+1][j].has_left_wall == False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j],True)

        if j<len(self._cells[0])-1 and self._cells[i][j+1].visited == False and self._cells[i][j+1].has_top_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1],True)
        return False

    def solve(self):
        return self._solve_r(0,0)