from CA import TwoDimensionalCA
from game_board import GameBoard
import pygame

pygame.init()

# Define the dimensions and rules for the cellular automaton
width = 50
height = 50
birth_rule = ["3"]
survival_rule = ["2", "3"]

# Create a TwoDimensionalCA instance
ca = TwoDimensionalCA(width, height, birth_rule, survival_rule)

# Create a GameBoard instance with the CA
pygame_sim = GameBoard(ca)

# Run the Pygame simulation
pygame_sim.run_simulation()