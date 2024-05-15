import pygame
import os
import shutil

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
zip_folder = 'fresh-food-vs-spoiled-food-classification'
questions_num = 0

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

buttons = [
    [Button(50, 150, images[0][0]), Button(500, 150, images[0][1])],
    [Button(500, 150, images[1][0]), Button(50, 150, images[1][1])],
    [Button(50, 150, images[2][0]), Button(500, 150, images[2][1])]
]

def display_question(screen, question, options, images):
    screen.fill((255, 255, 255))
    
    text_question = font.render(question, True, (0, 0, 0))
    screen.blit(text_question, (50, 50))
    if questions_num < len(questions):
        for i, option in enumerate(options[questions_num]):
            buttons[questions_num][i].draw(screen)

    pygame.display.flip()
def save_image(user_answer, question_num):
    image_path = f"image{question_num+1}_{user_answer}.png"
    print(user_answer)
    if user_answer == '1':
        save_folder = inner_folder
        destination_path = os.path.join(zip_folder, save_folder, image_path)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
        print(f"Изображение {user_answer} сохранено в папку {save_folder}: {image_path}")
        
        save_folder = "spoiled"
        user_answer = '2'
        image_path = f"image{question_num+1}_{user_answer}.png"
        destination_path = os.path.join(zip_folder, save_folder, image_path)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
        print(f"Изображение {user_answer} сохранено в папку {save_folder}: {image_path}")
    elif user_answer == '2':
        save_folder = inner_folder
        destination_path = os.path.join(zip_folder, save_folder, image_path)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
        print(f"Изображение {user_answer} сохранено в папку {save_folder}: {image_path}")
        
        save_folder = "spoiled"
        user_answer = '1'
        image_path = f"image{question_num+1}_{user_answer}.png"
        destination_path = os.path.join(zip_folder, save_folder, image_path)
        shutil.copy(os.path.join('images', 'quiz1_mc', image_path), destination_path)
        print(f"Изображение {user_answer} сохранено в папку {save_folder}: {image_path}")

def run_game():
    global questions_num
    running = True

    while running:
        if questions_num < len(questions):
            display_question(screen, questions[questions_num], options, images)
    
    
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
            
            running = False
            pygame.quit()
            #pygame.display.flip()

