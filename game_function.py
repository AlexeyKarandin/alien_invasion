# game_function.py
import sys
import pygame as pyg

def check_events():
    """
    Обрабатывает нажатия клавиш и события мыши
    :return:
    """
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
