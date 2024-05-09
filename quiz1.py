import pygame
import os
import sys
pygame.init()
questions = [
    "На каком из этих изображений присутствует свежий продукт питания?",
    "На каком из этих изображений присутствует свежий продукт питания?",
    "Что из этого не является тортом?"
]

options = [
    ["1", "2"],
    ["1", "2"],
    ["1", "2"]
]

answers = ["1", "2", "1"]

images = [
    [pygame.image.load(os.path.join('images', 'image1_1.png')), pygame.image.load(os.path.join('images', 'image1_2.png'))],  # Изображения для вопроса 1
    [pygame.image.load(os.path.join('images', 'image2_2.png')), pygame.image.load(os.path.join('images', 'image2_1.png'))],  # Изображения для вопроса 2
    [pygame.image.load(os.path.join('images', 'image3_1.png')), pygame.image.load(os.path.join('images', 'image3_2.png'))]   # Изображения для вопроса 3
]
guesses = []
score = 0
questions_num = 0

font = pygame.font.SysFont(None, 35)

def display_question(screen, question, options, images, image_positions):
    screen.fill((255, 255, 255))
    background_static = pygame.image.load(os.path.join('images', 'background.jpg'))
    bob = pygame.image.load(os.path.join('images', 'bob.png'))

    screen.blit(background_static, (0, 0))
    screen.blit(bob, (0, 0))

    for i, image in enumerate(images):
        screen.blit(image, image_positions[i])

    text_question = font.render(question, True, (255, 255, 0))
    screen.blit(text_question, (50, 50))

    y_position = 150
    for i, option in enumerate(options):
        text_option = font.render(option, True, (255, 255, 0))
        text_rect = text_option.get_rect(topleft=(50 if i == 0 else 500, y_position))
        
        if text_rect.collidepoint(pygame.mouse.get_pos()):
            text_option = font.render(option, True, (150, 150, 150))
        
        screen.blit(text_option, text_rect)
        
    pygame.display.flip()
