# alien_invasion.py

import pygame as pyg

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

    # Запуск основного цикла тгры.
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ship)
        ship.update()
        # обновление экрана
        gf.update_screen(ai_settings, screen, ship)


run_game()
