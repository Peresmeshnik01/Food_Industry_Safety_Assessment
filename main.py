import pygame
import sys
import os
from menu import menu_anim
import time
from TestQuiz import run_game
pygame.init()

WHITE = (255, 255, 255)
BLACK = (255, 255, 0)
GRAY = (150, 150, 150)


menu_anim()

time.sleep(1)
screen = pygame.display.set_mode((1000, 522))
pygame.display.set_caption("Quiz Game")
pygame.mixer.music.load(os.path.join("sounds", 'Quiz1.mp3'))
pygame.mixer.music.play(-1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        run_game()  

pygame.quit()
sys.exit()
