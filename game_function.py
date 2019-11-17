# game_function.py
import sys
import pygame as pyg
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатия клавиш"""
    if event.key == pyg.K_RIGHT:
        ship.moving_right = True
    elif event.key == pyg.K_LEFT:
        ship.moving_left = True
    elif event.key == pyg.K_UP:
        ship.moving_up = True
    elif event.key == pyg.K_DOWN:
        ship.moving_down = True
    elif event.key == pyg.K_SPACE:
        # Создание пули и добавление ее в группу bullets
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш"""
    if event.key == pyg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pyg.K_LEFT:
        ship.moving_left = False
    elif event.key == pyg.K_UP:
        ship.moving_up = False
    elif event.key == pyg.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """
    Обрабатывает нажатия клавиш и события мыши
    :return:
    """
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
        elif event.type == pyg.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pyg.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """
    Обновляет изображение на экране и отображает новый экран.
    :param ai_settings:
    :param screen:
    :param ship:
    :return:
    """
    # При каждом проходе цикла прорисовывается экран
    screen.fill(ai_settings.bg_color)
    # все пули выводятся позади изображения корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Отображение последнего прорисованного экрана.
    pyg.display.flip()
