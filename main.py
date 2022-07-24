from turtle import width
import pygame as pg
from screeninfo import get_monitors

HEIGHT = get_monitors()[0].height
WIDTH = get_monitors()[0].width

SCREEN = pg.display.set_mode((.6*WIDTH, .6*HEIGHT))

FPS = 60

def init_window():
    pg.display.set_caption('Shooter Game')
    SCREEN.fill((255, 255, 255))
    pg.display.update()


def main():

    clock = pg.time.Clock()

    while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT: return pg.quit()
        
        init_window()
        


if __name__ == '__main__':
    main()