from tkinter import Tk, BOTH, Canvas
from graphics import *
from cell import Cell
from maze import Maze

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    #line = Line(Point(100, 100), Point(400, 580))
    #cell = Cell(20,20,60,60, win.canvas_widget)
    #cell2 = Cell(60,20,100,60, win.canvas_widget)
    #cell.draw()
    #cell2.draw()
    #cell.draw_move(cell2)
    #win.draw_line(line, "red")
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()

    win.wait_for_close()

main()






