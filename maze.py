from cell import Cell
from graphics import *
import time, random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(i=0,j=0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
            # Check each direction
        # right
        if (i < self._num_cols - 1 and 
            not self._cells[i][j].has_right_wall and 
            not self._cells[i + 1][j].visited):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], True)  # undo
        
        # down
        if (j < self._num_rows - 1 and 
            not self._cells[i][j].has_bottom_wall and 
            not self._cells[i][j + 1].visited):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], True)  # undo
        
        # left
        if (i > 0 and 
            not self._cells[i][j].has_left_wall and 
            not self._cells[i - 1][j].visited):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], True)  # undo
        
        # up
        if (j > 0 and 
            not self._cells[i][j].has_top_wall and 
            not self._cells[i][j - 1].visited):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], True)  # undo
        
        return False

'''
class Maze():
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
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed != None:
            random.seed(seed)
        self.seed = seed
    
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        #self._reset_cells_visited()

    def _create_cells(self):
        self.cells = []
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(None)
            self.cells.append(col_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        cell = Cell(x1,y1,x2,y2,self.win.canvas_widget)
        self.cells[i][j] = cell
        cell.draw()
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return        
        self.win.redraw()
        time.sleep(0.002)
        
    def _break_entrance_and_exit(self):
        first_line_top = (self.x1, self.y1)
        first_line_bottom = (self.x1, self.y1 + self.cell_size_y)
        last_line_top = (self.x1 + ((self.num_cols-1) * self.cell_size_x), self.y1 + (self.num_rows * self.cell_size_y))
        last_line_bottom = (self.x1 + ((self.num_cols) * self.cell_size_x), self.y1 + (self.num_rows * self.cell_size_y))
        first_line = Line(Point(self.cells[0][0]._x1, self.cells[0][0]._y1), 
                    Point(self.cells[0][0]._x1, self.cells[0][0]._y2))
        last_line = Line(Point(self.cells[-1][-1]._x2, self.cells[-1][-1]._y1), 
                    Point(self.cells[-1][-1]._x2, self.cells[-1][-1]._y2))
        self.win.draw_line(first_line, "white")
        self.win.draw_line(last_line, "white")
    
    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            next_index_list = [];
            if j>0 and not self.cells[i][j-1].visited: #make sure the cell above us has visited set to False
                next_index_list.append((i,j-1)) #if the conditions are met, add the above cell to the list of unvisited_neighbors
            if j<self.num_rows-1 and not self.cells[i][j+1].visited: 
                next_index_list.append((i,j+1)) 
            if i < self.num_cols-1 and not self.cells[i+1][j].visited:
                next_index_list.append((i+1, j))
            if i > 0 and not self.cells[i-1][j].visited:
                next_index_list.append((i-1, j))
            if len(next_index_list) == 0:
                self._draw_cell(i,j)
                return
            next_cell = random.choice(next_index_list)
            self.cells[i][j].draw_move(self.cells[next_cell[0]][next_cell[1]])
            self._break_walls_r(next_cell[0], next_cell[1])



    
    def _reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False
        
'''

            




    


