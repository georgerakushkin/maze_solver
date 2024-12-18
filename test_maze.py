import unittest
from maze import Maze

class TestMaze(unittest.TestCase):
    def test_reset_cells_visited(self):
        # Create a small test maze
        maze = Maze(0, 0, 3, 3, 10, 10)
        
        # Set some cells as visited
        maze.cells[0][0].visited = True
        maze.cells[1][1].visited = True
        maze.cells[2][2].visited = True
        
        # Reset all cells
        maze._reset_cells_visited()
        
        # Check that all cells are now unvisited
        for i in range(maze.num_cols):
            for j in range(maze.num_rows):
                self.assertFalse(maze.cells[i][j].visited, 
                               f"Cell at ({i},{j}) should be unvisited")

if __name__ == '__main__':
    unittest.main()