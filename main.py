from graphics import Window, Line, Point
from cell import Cell
from maze import Maze
def main():
    win = Window(800,600)
    cell = Cell(win)
    cell.draw(10,100,500,200)
    cell2 = Cell(win)
    cell2.draw(150,300,550,400)
    cell.draw_move(cell2,True)
    

    test_maze = Maze(
        x1=50,           # start 50 pixels from left
        y1=50,           # start 50 pixels from top
        num_rows=10,     # 10 rows
        num_cols=10,     # 10 columns
        cell_size_x=40,  # each cell is 40 pixels wide
        cell_size_y=40,  # each cell is 40 pixels tall
        win=win          # the window to draw in
    )
    win.wait_for_close()

main()