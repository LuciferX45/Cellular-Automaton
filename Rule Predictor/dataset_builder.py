import numpy as np
from CA import TwoDimensionalCA
from drawing import DrawingBoard
import pygame

def build_dataset(width, height, birth_rule, survival_rule, filename):
    # Create a TwoDimensionalCA instance
    ca = TwoDimensionalCA(width, height, birth_rule, survival_rule)
    
    # Create a DrawingBoard instance
    drawing_board = DrawingBoard()
    
    # Run the drawing board to get the initial and final states
    drawing_board.run()
    initial_state = drawing_board.grid.copy()
    
    final_state = ca.evolve()
    print(final_state)

    with open(filename, "w", newline = '') as f:
        f.write(str(initial_state))
        f.write("\n")
        f.write(str(final_state))
    

# Example usage
pygame.init()
width = 10
height = 10
birth_rule = ['3']
survival_rule = ['2', '3']
generations = 10
filename = 'dataset.csv'
build_dataset(width, height, birth_rule, survival_rule, filename)

