import pygame 
import time
import numpy as np
from CA import TwoDimensionalCA
from game_board import GameBoard


pygame.init()

ca = TwoDimensionalCA(80,60,['3'],['2','3'])

gb = GameBoard(ca)

gb.run_simulation()