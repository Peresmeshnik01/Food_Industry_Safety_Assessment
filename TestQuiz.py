import pygame
import os
import shutil
import zipfile
import neural_network
import time
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 35)

questions = [
    "На каком из этих изображений присутствует свежий продукт питания?",
    "На каком из этих изображений присутствует свежий продукт питания?",
    "На каком из этих изображений присутствует свежий продукт питания?"
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
    text_question = font.render(question, True, (236, 236, 0))
    screen.blit(text_question, (50, 50))
    if questions_num < len(questions):
        for i, option in enumerate(options[questions_num]):
            buttons[questions_num][i].draw(screen)
    pygame.display.flip()
def save_image(user_answer, question_num):
    image_path = f"image{question_num+1}_{user_answer}.png"
    if user_answer == '1':
        save_folder = inner_folder
        new_image_name = f"image{question_num+1}_{save_folder}.png"
        destination_path = os.path.join('fresh-food-vs-spoiled-food-classification', 'train', save_folder, new_image_name)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
        
        save_folder = "spolied"
        user_answer = '2'
        image_path = f"image{question_num+1}_{user_answer}.png"
        new_image_name = f"image{question_num+1}_{save_folder}.png"
        destination_path = os.path.join('fresh-food-vs-spoiled-food-classification', 'train', save_folder, new_image_name)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
        
    elif user_answer == '2':
        save_folder = inner_folder
        new_image_name = f"image{question_num+1}_{save_folder}.png"
        destination_path = os.path.join('fresh-food-vs-spoiled-food-classification', 'train', save_folder, new_image_name)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
    
        save_folder = "spolied"
        user_answer = '1'
        image_path = f"image{question_num+1}_{user_answer}.png"
        new_image_name = f"image{question_num+1}_{save_folder}.png"
        destination_path = os.path.join('fresh-food-vs-spoiled-food-classification', 'train', save_folder, new_image_name)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
        
def display_text_pat(screen, text):
    background_static = pygame.image.load(os.path.join('images', 'background.jpg'))
    bob = pygame.image.load(os.path.join('images', 'bob.png'))
    pat = pygame.image.load(os.path.join('images', 'pat.png'))
    screen.blit(background_static, (0, 0))
    screen.blit(bob, (0, 0))
    screen.blit(pat, (0, 0))
    #screen.fill((255, 255, 255))
    text_surface = font.render(text, True, (255,156,165))
    text_rect = text_surface.get_rect(center=(700, 400))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def display_1Q(screen, text):
    background_static = pygame.image.load(os.path.join('images', 'background.jpg'))
    bob = pygame.image.load(os.path.join('images', 'bob.png'))
    pat = pygame.image.load(os.path.join('images', 'pat.png'))
    screen.blit(background_static, (0, 0))
    screen.blit(bob, (0, 0))
    screen.blit(pat, (0, 0))
    image1_fresh = pygame.image.load(os.path.join('fresh-food-vs-spoiled-food-classification/test1/1Q', 'image1_fresh.png'))
    image1_spoiled = pygame.image.load(os.path.join('fresh-food-vs-spoiled-food-classification/test1/1Q', 'image1_spolied.png'))

    # Отображение изображения image1_fresh в координатах (50, 150)
    screen.blit(image1_fresh, (500, 50))
    # Отображение изображения image1_spoiled в координатах (500, 150)
    screen.blit(image1_spoiled, (150, 50))
    text_surface = font.render(text, True, (255,156,165))
    text_rect = text_surface.get_rect(center=(600, 400))
    screen.blit(text_surface, text_rect)

    text_surface = font.render("На каком из этих изображений присутствует свежий продукт питания?", True, (236, 236, 0))
    text_rect = text_surface.get_rect(topleft=(50, 50))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
def display_2Q(screen, text):
    background_static = pygame.image.load(os.path.join('images', 'background.jpg'))
    bob = pygame.image.load(os.path.join('images', 'bob.png'))
    pat = pygame.image.load(os.path.join('images', 'pat.png'))
    screen.blit(background_static, (0, 0))
    screen.blit(bob, (0, 0))
    screen.blit(pat, (0, 0))
    image1_fresh = pygame.image.load(os.path.join('fresh-food-vs-spoiled-food-classification/test2/1Q', 'image2_fresh.png'))
    image1_spoiled = pygame.image.load(os.path.join('fresh-food-vs-spoiled-food-classification/test2/1Q', 'image2_spolied.png'))

    # Отображение изображения image1_fresh в координатах (50, 150)
    screen.blit(image1_fresh, (150, 50))
    # Отображение изображения image1_spoiled в координатах (500, 150)
    screen.blit(image1_spoiled, (500, 50))
    text_surface = font.render(text, True, (255,156,165))
    text_rect = text_surface.get_rect(center=(600, 400))
    screen.blit(text_surface, text_rect)

    text_surface = font.render("На каком из этих изображений присутствует свежий продукт питания?", True, (236, 236, 0))
    text_rect = text_surface.get_rect(topleft=(50, 50))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
def display_3Q(screen, text):
    background_static = pygame.image.load(os.path.join('images', 'background.jpg'))
    bob = pygame.image.load(os.path.join('images', 'bob.png'))
    pat = pygame.image.load(os.path.join('images', 'pat.png'))
    screen.blit(background_static, (0, 0))
    screen.blit(bob, (0, 0))
    screen.blit(pat, (0, 0))
    image1_fresh = pygame.image.load(os.path.join('fresh-food-vs-spoiled-food-classification/test3/1Q', 'image3_fresh.png'))
    image1_spoiled = pygame.image.load(os.path.join('fresh-food-vs-spoiled-food-classification/test3/1Q', 'image3_spolied.png'))

    # Отображение изображения image1_fresh в координатах (50, 150)
    screen.blit(image1_fresh, (150, 50))
    # Отображение изображения image1_spoiled в координатах (500, 150)
    screen.blit(image1_spoiled, (500, 50))
    text_surface = font.render(text, True, (255,156,165))
    text_rect = text_surface.get_rect(center=(600, 400))
    screen.blit(text_surface, text_rect)

    text_surface = font.render("На каком из этих изображений присутствует свежий продукт питания?", True, (236, 236, 0))
    text_rect = text_surface.get_rect(topleft=(50, 50))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def display_4Q(screen, text):
    background_static = pygame.image.load(os.path.join('images', 'background.jpg'))
    bob = pygame.image.load(os.path.join('images', 'bob.png'))
    pat = pygame.image.load(os.path.join('images', 'pat.png'))
    screen.blit(background_static, (0, 0))
    screen.blit(bob, (0, 0))
    screen.blit(pat, (0, 0))
    image1_fresh = pygame.image.load(os.path.join('fresh-food-vs-spoiled-food-classification/test4/1Q', 'image4_fresh.png'))
    image1_spoiled = pygame.image.load(os.path.join('fresh-food-vs-spoiled-food-classification/test4/1Q', 'image4_spolied.png'))

    # Отображение изображения image1_fresh в координатах (50, 150)
    screen.blit(image1_fresh, (500, 50))
    # Отображение изображения image1_spoiled в координатах (500, 150)
    screen.blit(image1_spoiled, (150, 50))
    text_surface = font.render(text, True, (255,156,165))
    text_rect = text_surface.get_rect(center=(600, 400))
    screen.blit(text_surface, text_rect)

    text_surface = font.render("На каком из этих изображений присутствует свежий продукт питания?", True, (236, 236, 0))
    text_rect = text_surface.get_rect(topleft=(50, 50))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
def display_5Q(screen, text):
    background_static = pygame.image.load(os.path.join('images', 'background.jpg'))
    bob = pygame.image.load(os.path.join('images', 'bob.png'))
    pat = pygame.image.load(os.path.join('images', 'pat.png'))
    screen.blit(background_static, (0, 0))
    screen.blit(bob, (0, 0))
    screen.blit(pat, (0, 0))
    image1_fresh = pygame.image.load(os.path.join('fresh-food-vs-spoiled-food-classification/test5/1Q', 'image5_fresh.png'))
    image1_spoiled = pygame.image.load(os.path.join('fresh-food-vs-spoiled-food-classification/test5/1Q', 'image5_spolied.png'))

    # Отображение изображения image1_fresh в координатах (50, 150)
    screen.blit(image1_fresh, (150, 50))
    # Отображение изображения image1_spoiled в координатах (500, 150)
    screen.blit(image1_spoiled, (500, 50))
    text_surface = font.render(text, True, (255,156,165))
    text_rect = text_surface.get_rect(center=(600, 400))
    screen.blit(text_surface, text_rect)

    text_surface = font.render("На каком из этих изображений присутствует свежий продукт питания?", True, (236, 236, 0))
    text_rect = text_surface.get_rect(topleft=(50, 50))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
def end1(screen):
    background_static = pygame.image.load(os.path.join('images', 'end1.PNG'))
    screen.blit(background_static, (0, 0)) 
    pygame.display.flip()

def end2(screen):
    background_static = pygame.image.load(os.path.join('images', 'end2.PNG'))
    screen.blit(background_static, (0, 0))
    pygame.display.flip()
def neural_work():
    self = 0
    display_1Q(screen, "думаю...")
    pygame.display.flip()
    train_dir = 'fresh-food-vs-spoiled-food-classification/train'
    val_dir = 'fresh-food-vs-spoiled-food-classification/val'
    test_dir = 'fresh-food-vs-spoiled-food-classification/test1'
    threshold = 0.5

    model = neural_network.train_model(train_dir, val_dir)
    predictions, filenames = neural_network.test_model(model, test_dir)  # Присваиваем возвращаемые значения переменным predictions и filenames
    for i, prediction in enumerate(predictions):
        if prediction[0] <= threshold:  # Предполагаемый класс - 0
            display_1Q(screen, "слева тухлый, справа свежий")
            self += 1
        else:
            display_1Q(screen, "слева свежий, справа тухлый")
    time.sleep(2)

    display_2Q(screen, "думаю...")
    model = neural_network.train_model(train_dir, val_dir)
    test_dir = 'fresh-food-vs-spoiled-food-classification/test2'
    predictions, filenames = neural_network.test_model(model, test_dir)
    for i, prediction in enumerate(predictions):
        if prediction[0] >= threshold:  # Предполагаемый класс - 0
            display_2Q(screen, "слева тухлый, справа свежий")
            self += 1
        else:
            display_2Q(screen, "слева свежий, справа тухлый")
    time.sleep(2)

    display_3Q(screen, "думаю...")
    model = neural_network.train_model(train_dir, val_dir)
    test_dir = 'fresh-food-vs-spoiled-food-classification/test3'
    predictions, filenames = neural_network.test_model(model, test_dir)
    for i, prediction in enumerate(predictions):
        if prediction[0] <= threshold:  # Предполагаемый класс - 0
            display_3Q(screen, "слева тухлый, справа свежий")
        else:
            display_3Q(screen, "слева свежий, справа тухлый")
            self+=1
    time.sleep(2)

    display_4Q(screen, "думаю...")
    model = neural_network.train_model(train_dir, val_dir)
    test_dir = 'fresh-food-vs-spoiled-food-classification/test4'
    predictions, filenames = neural_network.test_model(model, test_dir)
    for i, prediction in enumerate(predictions):
        if prediction[0] <= threshold:  # Предполагаемый класс - 0
            display_4Q(screen, "слева тухлый, справа свежий")
            self+=1
        else:
            display_4Q(screen, "слева свежий, справа тухлый")
    time.sleep(2)
    
    display_5Q(screen, "думаю...")
    model = neural_network.train_model(train_dir, val_dir)
    test_dir = 'fresh-food-vs-spoiled-food-classification/test5'
    predictions, filenames = neural_network.test_model(model, test_dir)
    for i, prediction in enumerate(predictions):
        if prediction[0] <= threshold:  # Предполагаемый класс - 0
            display_5Q(screen, "слева тухлый, справа свежий")
        else:
            display_5Q(screen, "слева свежий, справа тухлый")
            self+=1
    time.sleep(4)
    if self <= 3:
        end1(screen)
        time.sleep(4)
    else:
        end2(screen)
        time.sleep(4)
    pygame.quit()
