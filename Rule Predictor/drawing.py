import numpy as np 
import pygame

# Constants
GRID_SIZE = 10 # Size of each cell in pixels
GRID_WIDTH = 80  # Number of cells in the grid (width)
GRID_HEIGHT = 60  # Number of cells in the grid (height)
WINDOW_SIZE = (GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE)  # Window size


# Colors
bg_color = (0, 0, 0)
grid_color = (128, 128, 128)
cell_color = (255, 255, 255)

class DrawingBoard:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Cellular Automaton Drawing Board")
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
        self.drawing = False
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.drawing = False
            elif event.type == pygame.MOUSEMOTION and self.drawing:
                x, y = event.pos
                row = y // GRID_SIZE
                col = x // GRID_SIZE
                if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
                    self.grid[row][col] = 1
                else:
                    print(f"Warning: Coordinates (row={row}, col={col}) are out of bounds.")
                

    def draw_grid(self):
        self.screen.fill(bg_color)

        # Draw vertical grid lines
        for col in range(0, GRID_WIDTH * GRID_SIZE, GRID_SIZE):
            pygame.draw.line(self.screen, grid_color, (col, 0), (col, WINDOW_SIZE[1]))

        # Draw horizontal grid lines
        for row in range(0, GRID_HEIGHT * GRID_SIZE, GRID_SIZE):
            pygame.draw.line(self.screen, grid_color, (0, row), (WINDOW_SIZE[0], row))

        # Draw cells based on the grid state
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if self.grid[row][col] == 1:
                    pygame.draw.rect(self.screen, cell_color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def run(self):
        while self.running:
            self.handle_events()
            self.screen.fill(bg_color)
            self.draw_grid()
            pygame.display.flip()

        pygame.quit()



        