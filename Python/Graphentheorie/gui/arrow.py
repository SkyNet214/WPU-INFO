import pygame as pg
pg.init()

screen = pg.display.set_mode((1920, 1080))

while True:
    pg.draw.polygon(screen, (255, 255, 255), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))

    pg.display.update()