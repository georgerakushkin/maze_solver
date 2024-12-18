from graphics import *
import time

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def cell_center_point(point1, point2):
        center_x = (point1.x + point2.x)/2
        center_y = (point1.y + point2.y)/2
        return center_x, center_y
    
    def draw_move(self, to_cell, undo = False):
        if undo == False:
            line_color = "red"
        else:
            line_color = "gray"
        our_center_x = (self._x1 + self._x2)/2
        our_center_y = (self._y1 + self._y2)/2
        other_center_x = (to_cell._x1 + to_cell._x2)/2
        other_center_y = (to_cell._y1 + to_cell._y2)/2
        line_s = Point(our_center_x, our_center_y)
        line_e = Point(other_center_x, other_center_y)
        line = Line(line_s, line_e)
        line.draw(self._win.canvas_widget, line_color)

