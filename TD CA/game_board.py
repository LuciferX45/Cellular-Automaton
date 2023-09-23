import pygame
import numpy as np
import time

class GameBoard:
    def __init__(self, ca, cell_size = 10):
        self.width = ca.width
        self.height = ca.height
        self.cell_size = cell_size
        
        self.screen = pygame.display.set_mode((self.width*self.cell_size, 
                                               self.height*self.cell_size))
        pygame.display.set_caption("Cellular Automaton Simulation")
        
        self.clock = pygame.time.Clock()
        self.grid_board = ca.grid
        self.running = False
        
        self.color_bg = (10,10,10)
        self.color_grid = (60,60,60)
        self.color_die_next = (180,180,180)
        self.color_alive = (255,255,255)    
        
        
    def toggle_simulation(self):
        self.running = not self.running
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.toggle_simulation()
            
            
            if self.running:
                if pygame.key.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    col = pos[0]//self.cell_size
                    row = pos[0]//self.cell_size
            