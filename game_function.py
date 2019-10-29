# game_function.py
import sys
import pygame as pyg

def check_keydown_events(event, ship):
    """Реагирует на нажатия клавиш"""
    if event.key == pyg.K_RIGHT:
        ship.moving_right = True
    elif event.key == pyg.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш"""
    if event.key == pyg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pyg.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """
    Обрабатывает нажатия клавиш и события мыши
    :return:
    """
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
        elif event.type == pyg.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pyg.KEYUP:
            check_keyup_events(event, ship)

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
