import sys
import os

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pygame
from player import HumanPlayer
from screen import Screen
from game import Game , HardGame
from main import play_game

if __name__ == "__main__":
    pygame.init()
    screen = Screen()
    player = HumanPlayer(screen.width / 2, screen.height - 100)
    game = Game(max_enemies=20)

    play_game(screen, player, game)
