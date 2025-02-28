from graphics import Window, Line, Point

def main():
    win = Window(800,600)

    win.draw_line(Line(Point(10,150), Point(500,10)), 'black')
    win.wait_for_close()
main()