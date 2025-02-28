from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("window")
        self.canvas = Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack()
        self.running = False
        self.root.protocol('WM_DELETE_WINDOW', self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print('window closed')

    def close(self):
        self.running = False

    def draw_line(self, line, colour='black'):
        line.draw(self.canvas, colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    def draw(self, canvas, colour):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill = colour, width =2)
        
class Cell:
    def __init__(self, x1, x2, y1, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window
    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        if self.has_left_wall:
            self._win.draw_line(Line(top_left,bottom_left))
        if self.has_right_wall:
            self._win.draw_line(Line(top_right,bottom_right))
        if self.has_top_wall:
            self._win.draw_line(Line(top_left,top_right))
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left,bottom_right))
        