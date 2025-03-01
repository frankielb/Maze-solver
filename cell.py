from graphics import Line, Point

class Cell:
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        if self.has_left_wall:
            self._win.draw_line(Line(top_left,bottom_left))
        else:
            self._win.draw_line(Line(top_left,bottom_left),'white')
        if self.has_right_wall:
            self._win.draw_line(Line(top_right,bottom_right))
        else:
            self._win.draw_line(Line(top_right,bottom_right),'white')
        if self.has_top_wall:
            self._win.draw_line(Line(top_left,top_right))
        else:
            self._win.draw_line(Line(top_left,top_right),'white')
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left,bottom_right))
        else:
            self._win.draw_line(Line(bottom_left,bottom_right),'white')
    def draw_move(self, to_cell, undo=False):
        if undo:
            colour = 'gray'
        else:
            colour = 'red'
        def get_mid(x1,x2,y1,y2):
            x = (x1 + x2)/2
            y = (y1 + y2)/2
            return Point(x,y)
        from_mid = get_mid(self._x1, self._x2, self._y1, self._y2)
        to_mid = get_mid(to_cell._x1, to_cell._x2, to_cell._y1, to_cell._y2)
        self._win.draw_line(Line(from_mid,to_mid), colour)