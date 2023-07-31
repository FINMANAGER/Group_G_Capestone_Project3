# Import the pygame library for visualisation (assumed to be installed).
import pygame

# Import the Cell class from the cell.py module.
from cell import Cell

# The Maze class represents a maze and is used to generate a random maze

class Maze:
    # Constructor to initialise the maze with the number of columns (cols) and rows (rows).
    def __init__(self, cols, rows):
        # Store the number of columns and rows.
        self.cols = cols
        self.rows = rows

        # Thickness of the walls in the maze/
        self.thickness = 4

        # Create a list of Cell objects representing the grid of the maze.
        self.grid_cells = [Cell(col, row, self.thickness) for row in range(self.rows) for col in range(self.cols)]

    # Method to remove walls between two neighboring cells to create paths in the maze.
    def remove_walls(self, current, next):
        # Calculate the difference in x and y positions between the cells.
        dx = current.x - next.x
        # If the cells are horizontally adjancent, update the walls accordingly.
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y

        # If the cells are veritcally adjacent, update the walls acooringly.
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False

    # Method to generate the maze.
    def generate_maze(self):
        # Start generating the maze from the first cell in the grid.
        current_cell = self.grid_cells[0]

        # List to store the visited cells in order to backtrack later.
        array = []

        # Counter to keep track of the number of cells visited.
        break_count = 1

        # Continue generating the maze until all vells have been visited.
        while break_count != len(self.grid_cells):
            # Mark the current cell as visited.
            current_cell.visited = True

            # Check for unvisited neighbors of the current cell.
            next_cell = current_cell.check_neighbors(self.cols, self.rows, self.grid_cells)

            # If a neighboring cell is found, move to it and update the walls.
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                self.remove_walls(current_cell, next_cell)
                current_cell = next_cell
                # if no unvisited neighbor is found, backtrack to the last visited cell.
            elif array:
                current_cell = array.pop()

        # Return the list of grid cells representing the generated maze.
        return self.grid_cells
