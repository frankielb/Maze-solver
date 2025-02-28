from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800,600)
    cell = Cell(win)
    cell.draw(10,100,500,200)
    cell2 = Cell(win)
    cell2.draw(150,300,550,400)
    cell.draw_move(cell2,True)
    win.wait_for_close()
main()