import pygame as pg
from screeninfo import get_monitors
import os


WIDTH = .6*get_monitors()[0].width
HEIGHT = .6*get_monitors()[0].height

S_WIDTH = .06*HEIGHT
S_HEIGHT = .05*HEIGHT

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

FPS = 60

def init_window(rec_1, rec_2):
    pg.display.set_caption('Shooter Game')
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(get_ship(1), (rec_1.x, rec_1.y))
    SCREEN.blit(get_ship(2), (rec_2.x, rec_2.y))
    pg.display.update()


def get_ship(ship: int):
    image = pg.image.load(
        os.path.join('assets', 'ship_' + str(ship) + '.png')
    )
    image = pg.transform.scale(image, (S_WIDTH, S_HEIGHT))
    image = pg.transform.rotate(image, (90 if ship == 1 else 270))
    return image


def main():
    clock = pg.time.Clock()

    rec_1 = pg.Rect(.15*WIDTH, HEIGHT/2.2, S_WIDTH, S_HEIGHT)
    rec_2 = pg.Rect(.85*WIDTH, HEIGHT/2.2, S_WIDTH, S_HEIGHT)

    while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT: return pg.quit()
        
        init_window(rec_1, rec_2)        


if __name__ == '__main__':
    main()