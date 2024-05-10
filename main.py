import pygame
import sys
import os
import rez1
from quiz1 import questions, guesses, options, answers, images, font, display_question

pygame.init()

# Инициализация окна
screen = pygame.display.set_mode((1000, 522))
pygame.display.set_caption("Quiz Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (255, 255, 0)
GRAY = (150, 150, 150)

running = True
image_positions = [(70, 50), (520, 50)]  # Пример координат для двух изображений
questions_num = 0

while running and questions_num < len(questions):
    current_question = questions[questions_num]
    current_options = options[questions_num]
    current_images = images[questions_num]
    display_question(screen, current_question, current_options, current_images, image_positions)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, option in enumerate(current_options):
                text_rect = font.render(option, True, BLACK).get_rect(topleft=(50 if i == 0 else 500, 150 + i))
                if text_rect.collidepoint(pygame.mouse.get_pos()):
                    choice = option

                    questions_num += 1
            file_path = 'quiz1_result.csv'
            rez1.save_results_to_csv(guesses, answers, file_path)
pygame.quit()
sys.exit()
