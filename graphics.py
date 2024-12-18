from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title("Maze Solver")
        self.canvas_widget = Canvas(
            self.root_widget,
            bg="white",
            width=width,
            height=height
        )
        self.canvas_widget.pack(fill=BOTH, expand=True)
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
    
    def close(self):
        self.running = False


    def draw_line(self, line, fill_color = "black"):
        line.draw(self.canvas_widget, fill_color )

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1  # First endpoint of the line
        self.point2 = point2  # Second endpoint of the line
    
    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2
        )   


        