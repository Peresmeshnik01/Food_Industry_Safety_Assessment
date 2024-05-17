import pygame
import sys
import os
from menu import menu_anim
import time
import shutil
from TestQuiz import display_question, screen, questions, questions_num, options, images, buttons, save_image
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
    global questions_num
    if questions_num < len(questions):
        display_question(screen, questions[questions_num], options, images, questions_num)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, button in enumerate(buttons[questions_num]):
                if button.rect.collidepoint(event.pos):
                    user_answer = options[questions_num][i]
                    save_image(user_answer, questions_num)
                    questions_num += 1
                     
    if questions_num >= len(questions):
        print("Вопросы закончились")
        # Конвертация папки в zip-архив
        folder_to_zip = "fresh-food-vs-spoiled-food-classification"
        zip_filename = "fresh-food-vs-spoiled-food-classification.zip"

        shutil.make_archive(zip_filename, 'zip', folder_to_zip)
        print(f"Папка {folder_to_zip} успешно сконвертирована в zip-архив {zip_filename}.")    
        running = False
        pygame.quit()
            #pygame.display.flip()

