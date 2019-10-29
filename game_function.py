# game_function.py
import sys

import pygame as pyg


def check_events(ship):
    """
    Обрабатывает нажатия клавиш и события мыши
    :return:
    """
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_RIGHT:
               ship.moving_right = True
            elif event.key == pyg.K_LEFT:
                #переместить корабль в лево
                ship.moving_left = True

        elif event.type == pyg.KEYUP:
            if event.key == pyg.K_RIGHT:
                ship.moving_right = False
            elif event.key == pyg.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """
    Обновляет изображение на экране и отображает новый экран.
    :param ai_settings:
    :param screen:
    :param ship:
    :return:
    """
    # При каждом проходе цикла прорисовывается экран
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Отображение последнего прорисованного экрана.
    pyg.display.flip()
