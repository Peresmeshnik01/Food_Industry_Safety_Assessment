import pygame
import os
import shutil
import zipfile

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 35)

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
    [pygame.image.load(os.path.join('images', 'quiz1_mc', 'image1_1.png')), pygame.image.load(os.path.join('images', 'quiz1_mc', 'image1_2.png')), 'image1'],
    [pygame.image.load(os.path.join('images', 'quiz1_mc', 'image2_1.png')), pygame.image.load(os.path.join('images', 'quiz1_mc', 'image2_2.png')), 'image2'],
    [pygame.image.load(os.path.join('images', 'quiz1_mc', 'image3_1.png')), pygame.image.load(os.path.join('images', 'quiz1_mc', 'image3_2.png')), 'image3']
]

inner_folder = 'fresh'
zip_folder = 'fresh-food-vs-spoiled-food-classification\train'
questions_num = 0

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

buttons = [
    [Button(150, 50, images[0][0]), Button(500, 50, images[0][1])],
    [Button(500, 50, images[1][0]), Button(150, 50, images[1][1])],
    [Button(150, 50, images[2][0]), Button(500, 50, images[2][1])]
]

def display_question(screen, question, options, images, questions_num):
    screen.fill((255, 255, 255))
    background_static = pygame.image.load(os.path.join('images', 'background.jpg'))
    bob = pygame.image.load(os.path.join('images', 'bob.png'))
    pat = pygame.image.load(os.path.join('images', 'pat.png'))
    screen.blit(background_static, (0, 0))
    screen.blit(bob, (0, 0))
    screen.blit(pat, (0, 0))
    text_question = font.render(question, True, (255, 255, 0))
    screen.blit(text_question, (50, 50))
    if questions_num < len(questions):
        for i, option in enumerate(options[questions_num]):
            buttons[questions_num][i].draw(screen)

    pygame.display.flip()
def save_image(user_answer, question_num):
    image_path = f"image{question_num+1}_{user_answer}.png"
    #print(user_answer)
    if user_answer == '1':
        save_folder = inner_folder
        new_image_name = f"image{question_num+1}_{save_folder}.png"
        destination_path = os.path.join('fresh-food-vs-spoiled-food-classification', 'train', save_folder, new_image_name)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
        
        print(f"Спанч Боб: {user_answer} относится к свежему продукту {save_folder}: {image_path}")
        
        save_folder = "spolied"
        user_answer = '2'
        image_path = f"image{question_num+1}_{user_answer}.png"
        new_image_name = f"image{question_num+1}_{save_folder}.png"
        destination_path = os.path.join('fresh-food-vs-spoiled-food-classification', 'train', save_folder, new_image_name)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
        
        
        print(f"Спанч Боб: {user_answer} относится к испорченному продукту {save_folder}: {image_path}")
    elif user_answer == '2':
        save_folder = inner_folder
        new_image_name = f"image{question_num+1}_{save_folder}.png"
        destination_path = os.path.join('fresh-food-vs-spoiled-food-classification', 'train', save_folder, new_image_name)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
       
        print(f"Спанч Боб: {user_answer} относится к свежему продукту {save_folder}: {image_path}")
        
        save_folder = "spolied"
        user_answer = '1'
        image_path = f"image{question_num+1}_{user_answer}.png"
        new_image_name = f"image{question_num+1}_{save_folder}.png"
        destination_path = os.path.join('fresh-food-vs-spoiled-food-classification', 'train', save_folder, new_image_name)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
        
        print(f"Спанч Боб: {user_answer} относится к испорченному продукту {save_folder}: {image_path}")

