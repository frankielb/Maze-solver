from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800,600)
    cell = Cell(win)
    cell.draw(10,100,500,200)

    win.wait_for_close()
main()