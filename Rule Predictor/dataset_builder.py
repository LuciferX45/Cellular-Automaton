import numpy as np
import pygame
import csv
from CA import TwoDimensionalCA
from drawing import DrawingBoard

# Constants
RULES = [
    ("B3/S23", "B3/S23"),  # Example rule format
    ("B1/S1", "B1/S1"),
    # Add more rules as needed
]
DATASET_SIZE = 100  # Number of examples in the dataset
CSV_FILE = "cellular_automaton_dataset.csv"  # Name of the CSV file

# Initialize Pygame
pygame.init()

# Function to generate and save a dataset as a CSV file
def build_and_save_dataset():
    dataset = []

    for rule in RULES:
        initial_state = np.random.randint(2, size=(GRID_HEIGHT, GRID_WIDTH))  # Random initial state

        # Create a cellular automaton with the specified rule
        ca = TwoDimensionalCA(GRID_WIDTH, GRID_HEIGHT, birth_rule=rule[0], survival_rule=rule[1])
        ca.grid = initial_state

        # Simulate the cellular automaton and visualize it
        for _ in range(10):  # You can adjust the number of generations
            ca.evolve()

        final_state = ca.grid  # Final state after simulation

        dataset.append((rule[0], rule[1], initial_state, final_state))

    # Save the dataset as a CSV file
    with open(CSV_FILE, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Birth Rule", "Survival Rule", "Initial State", "Final State"])
        for example in dataset:
            birth_rule, survival_rule, initial_state, final_state = example
            csv_writer.writerow([birth_rule, survival_rule, initial_state, final_state])

if __name__ == "__main__":
    GRID_WIDTH = 80
    GRID_HEIGHT = 60

    build_and_save_dataset()

    # Quit Pygame
    pygame.quit()
