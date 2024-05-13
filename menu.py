import pygame
import sys
from moviepy.editor import VideoFileClip, AudioFileClip
import time
import os

def menu_anim():
    pygame.init()
    pygame.display.set_caption("Quiz Game")
    window_size = (704, 400)
    screen = pygame.display.set_mode(window_size)

    pygame.mixer.init()
    sound_folder = "sounds"
    file_name = "Пальма.mp3"
    file_path = os.path.join(sound_folder, file_name)

    theme_music = pygame.mixer.Sound(file_path)
    theme_channel = pygame.mixer.Channel(0)
    theme_channel.play(theme_music, loops=-1)
    
    pygame.mixer.music.load(os.path.join("sounds", 'ВыГотовыДети.mp3'))
    pygame.mixer.music.play()
    background_image = pygame.image.load(os.path.join("menu", 'menu.png'))
    background_image = pygame.transform.scale(background_image, window_size)
    WHITE = (255, 255, 255)  

    
    font = pygame.font.Font(None, 36)

    
    game_title_text = font.render("Губка Боб и безопасность пищевой промышленности", True, WHITE)
    game_title_rect = game_title_text.get_rect(center=(window_size[0]//2, 50))

    
    start_button_text = font.render("Готовы!", True, WHITE)
    start_button_rect = start_button_text.get_rect(center=(window_size[0]//2, window_size[1]-50))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos):
                sound_folder = "sounds"
                file_name = "ДаКапитан.mp3"
                file_path = os.path.join(sound_folder, file_name)
                button_click_sound = pygame.mixer.Sound(file_path)
                button_click_sound.play()

                time.sleep(1)  
                running = False

        
        screen.blit(background_image, (0, 0))
        screen.blit(game_title_text, game_title_rect)
        screen.blit(start_button_text, start_button_rect)
       
        pygame.display.flip()

       
    video_path = os.path.join("menu", "introduction.mp4")

    sound_folder = "sounds"
    background_music_file = "ТемаМеню.mp3"
    background_music_path = os.path.join(sound_folder, background_music_file)

    video = VideoFileClip(video_path)
    background_music = AudioFileClip(background_music_path)
    background_music = background_music.set_duration(video.duration)
    video_with_music = video.set_audio(background_music)
    video_with_music.preview()
    pygame.mixer.music.stop()
    pygame.display.flip()

