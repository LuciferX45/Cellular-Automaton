import pygame 
import time
import numpy as np
from CA import TwoDimensionalCA
from game_board import GameBoard

pygame.init()

ca = TwoDimensionalCA(100,70,['3'],['2','3'])
#B345/S0456
#0123478/S01234678
#B0123478/S34678
#B1/S134567

gb = GameBoard(ca)

gb.run_simulation()