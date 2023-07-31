import pygame
from random import choice
# import pygame: This line imports the Pygame library, which is used for creating games and graphics applications. The code is likely using Pygame for visualizing the maze on the screen.
# from random import choice: This line imports the choice function from the random module. The choice function is used to randomly select an element from a list.
class Cell:
    def __init__(self, x, y, thickness):
        self.x, self.y = x, y
        self.thickness = thickness
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
      # class Cell:: The code defines a class named Cell, which represents a single cell in the maze grid.
# Constructor (__init__ method):
       # draw grid cell walls
    def draw(self, sc, tile):
        x, y = self.x * tile, self.y * tile
        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('darkgreen'), (x, y), (x + tile, y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('darkgreen'), (x + tile, y), (x + tile, y + tile), self.thickness)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('darkgreen'), (x + tile, y + tile), (x , y + tile), self.thickness)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('darkgreen'), (x, y + tile), (x, y), self.thickness)
          # checks if cell does exist and returns it if it does
    def check_cell(self, x, y, cols, rows, grid_cells):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x, y)]

    # checking cell neighbors of current cell if visited (carved) or not
    def check_neighbors(self, cols, rows, grid_cells):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1, cols, rows, grid_cells)
        right = self.check_cell(self.x + 1, self.y, cols, rows, grid_cells)
        bottom = self.check_cell(self.x, self.y + 1, cols, rows, grid_cells)
        left = self.check_cell(self.x - 1, self.y, cols, rows, grid_cells)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False



# Class Definition:



# def __init__(self, x, y, thickness):: This is the constructor method of the Cell class. It is executed when a new Cell object is created.
# The constructor takes three arguments:
# x: The x-coordinate (column) of the cell in the grid.
# y: The y-coordinate (row) of the cell in the grid.
# thickness: The thickness of the walls when drawing the cell.
# The constructor initializes various attributes of the Cell object:
# self.x and self.y: Store the x and y coordinates of the cell.
# self.thickness: Store the thickness of the cell's walls.
# self.walls: A dictionary that represents the walls of the cell. It contains four keys: 'top', 'right', 'bottom', and 'left'. Each key maps to a boolean value (True or False) indicating whether the corresponding wall is present or not.
# self.visited: A boolean flag to track whether the cell has been visited during maze generation. Initially, it is set to False.
# Draw Method (draw):

# def draw(self, sc, tile):: This method is responsible for drawing the walls of the cell on the screen.
# The method takes two arguments:
# sc: The screen or surface on which to draw the walls.
# tile: The size of a single cell (tile) in pixels.
# The method calculates the pixel coordinates of the top-left corner of the cell (x, y) based on its grid position (self.x, self.y) and the size of each cell (tile).
# Using pygame.draw.line, the method draws the four walls of the cell if they are present (True in self.walls).
# Top wall: Draws a line from (x, y) to (x + tile, y).
# Right wall: Draws a line from (x + tile, y) to (x + tile, y + tile).
# Bottom wall: Draws a line from (x + tile, y + tile) to (x, y + tile).
# Left wall: Draws a line from (x, y + tile) to (x, y).
# Check Cell Method (check_cell):

# def check_cell(self, x, y, cols, rows, grid_cells):: This method is used to check if a cell exists at a specified position in the grid and return the cell object if it exists.
# The method takes five arguments:
# x: The x-coordinate (column) of the cell to check.
# y: The y-coordinate (row) of the cell to check.
# cols: The total number of columns in the grid.
# rows: The total number of rows in the grid.
# grid_cells: A list containing all the cells in the grid.
# The method calculates a 1D index (find_index) from the 2D coordinates x and y using a lambda function.
# It checks if the calculated index is within the grid boundaries. If it is, the method returns the cell object from the grid_cells list at the calculated index. Otherwise, it returns False.
# Check Neighbors Method (check_neighbors):

# def check_neighbors(self, cols, rows, grid_cells):: This method checks neighboring cells of the current cell to find unvisited neighbors.
# The method takes three arguments:
# cols: The total number of columns in the grid.
# rows: The total number of rows in the grid.
# grid_cells: A list containing all the cells in the grid.
# The method checks the neighboring cells in four directions: top, right, bottom, and left.
# For each neighboring cell, it checks if the cell is within the grid boundaries and if it is unvisited (not visited). If both conditions are met, the neighboring cell is added to the neighbors list.
# Finally, the method returns a randomly chosen unvisited neighbor from the neighbors list using the choice function. If there are no unvisited neighbors, it returns False.
