# alien_invasion.py

import pygame as pyg
from pygame.sprite import Group

import game_function as gf
from settings import Settings
from ship import Ship

def run_game():
    # инициализирует игру и создает объект экрана
    pyg.init()
    ai_settings = Settings()
    screen = pyg.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
    pyg.display.set_caption("Alien invansion")
    # Создание корабля
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль
    bullets = Group()

    # Запуск основного цикла тгры.
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        # Обновление корабля и пуль
        ship.update()
        gf.update_bullets(bullets)
        # обновление экрана
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
