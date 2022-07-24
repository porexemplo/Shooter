import pygame as pg
from screeninfo import get_monitors
import os


WIDTH = .6*get_monitors()[0].width
HEIGHT = .6*get_monitors()[0].height

S_WIDTH = .06*HEIGHT
S_HEIGHT = .05*HEIGHT

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

FPS = 60

def init_window():
    pg.display.set_caption('Shooter Game')
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(get_ship(1).get('sprite'), get_ship(1).get('position'))
    SCREEN.blit(get_ship(2).get('sprite'), get_ship(2).get('position'))
    pg.display.update()


def get_ship(ship: int):
    image = pg.image.load(
        os.path.join('assets', 'ship_' + str(ship) + '.png')
    )
    image = pg.transform.scale(image, (S_WIDTH, S_HEIGHT))
    image = pg.transform.rotate(image, (90 if ship == 1 else 270))
    return {
        'sprite': image,
        'position': (abs((ship-1)*WIDTH - .15*WIDTH), HEIGHT/2.5)
    }


def main():

    clock = pg.time.Clock()


    while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT: return pg.quit()
        
        init_window()
        


if __name__ == '__main__':
    main()