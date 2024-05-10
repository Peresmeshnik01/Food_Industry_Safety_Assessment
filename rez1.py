import pygame
import os
import sys
import csv
from quiz1 import guesses, answers

pygame.init()
# Определение пути к файлу, куда будут сохраняться результаты


# Функция для сохранения результатов в CSV файл
def save_results_to_csv(guesses, answers, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player_Guess', 'Correct_Answer'])
        for guess, answer in zip(guesses, answers):
            writer.writerow([guess, answer])
