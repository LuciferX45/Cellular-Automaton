import time
import pygame
import numpy as np

color_bg = (10, 10, 10)
color_grid = (60, 60, 60)
color_prey = (255, 255, 255)        # Color for prey (rabbits)
color_predator = (255, 0, 0)        # Color for predators (foxes)
color_die_next = (180, 180, 180)

def update(screen, cells, size, with_progress=False):
    # Taking shape of the cells in the grid
    update_cells = np.zeros((cells.shape[0], cells.shape[1]))

    # Updating the cells individually by the rules
    for row, col in np.ndindex(cells.shape):

        # Count alive prey and predators around the current cell
        prey_around = np.sum((cells[max(row-1, 0):min(row+2, cells.shape[0]), 
                                   max(col-1, 0):min(col+2, cells.shape[1])] == 1))
        predator_around = np.sum((cells[max(row-1, 0):min(row+2, cells.shape[0]), 
                                        max(col-1, 0):min(col+2, cells.shape[1])] == 2))

        # Sets color
        color = color_bg if cells[row, col] == 0 else color_prey if cells[row, col] == 1 else color_predator

        # Checking the rules for prey and predators
        if cells[row, col] == 1:   # Prey (rabbits)
            if predator_around > 0:
                cells[row, col] = 0    # Prey is eaten by a predator
                if with_progress:
                    color = color_die_next
            else:
                # Prey can move randomly to an adjacent empty cell (optional)
                move_row, move_col = np.random.randint(-1, 2), np.random.randint(-1, 2)
                new_row, new_col = row + move_row, col + move_col
                if 0 <= new_row < cells.shape[0] and 0 <= new_col < cells.shape[1] and cells[new_row, new_col] == 0:
                    cells[new_row, new_col] = 1
                    cells[row, col] = 0
                    if with_progress:
                        color = color_bg
        elif cells[row, col] == 2:   # Predator (foxes)
            if prey_around > 0:
                cells[row, col] = 0    # Predator eats prey
                if with_progress:
                    color = color_die_next
            else:
                # Predator can move randomly to an adjacent empty cell (optional)
                move_row, move_col = np.random.randint(-1, 2), np.random.randint(-1, 2)
                new_row, new_col = row + move_row, col + move_col
                if 0 <= new_row < cells.shape[0] and 0 <= new_col < cells.shape[1] and cells[new_row, new_col] == 0:
                    cells[new_row, new_col] = 2
                    cells[row, col] = 0
                    if with_progress:
                        color = color_bg

        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))

    return update_cells

def random_assignment(cells, num_prey, num_predators):
    prey_locations = np.random.choice(np.arange(cells.size), num_prey, replace=False)
    predator_locations = np.random.choice(np.arange(cells.size), num_predators, replace=False)
    cells.ravel()[prey_locations] = 1
    cells.ravel()[predator_locations] = 2

def main():
    pygame.init()
    
    # Set up the screen
    screen = pygame.display.set_mode((800, 600))

    # Define the grid of cells (0: empty, 1: prey, 2: predator)
    cells = np.zeros((60, 80))
    num_prey = 200
    num_predators = 20
    random_assignment(cells, num_prey, num_predators)
    
    screen.fill(color_grid)
    
    # Update the screen with the initial state of cells
    update(screen, cells, 10)

    # Update the display
    pygame.display.flip()
    pygame.display.update()

    running = False
    
    # Game loop
    while True:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Toggle the running state when the space key is pressed
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()

        screen.fill(color_grid)

        if running:
            cells = update(screen, cells, 10)
            pygame.display.update()
            
        time.sleep(0.00000001)
        
if __name__ == "__main__":
    main()
