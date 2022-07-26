import pygame as pg
from screeninfo import get_monitors
import os


WIDTH = .6*get_monitors()[0].width
HEIGHT = .6*get_monitors()[0].height

S_WIDTH = .06*HEIGHT
S_HEIGHT = .05*HEIGHT

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

BORDER = pg.Rect(WIDTH/2 - .005*WIDTH , 0, .01*WIDTH, HEIGHT)

FPS = 60
VEL = .006*WIDTH

def init_window(rec_1, rec_2):
    pg.display.set_caption('Shooter Game')
    SCREEN.fill((255, 255, 255))
    pg.draw.rect(SCREEN, (0, 0, 0), BORDER)
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


def move_ship_1(pressed_keys, ship):
    if pressed_keys[pg.K_a] and ship.x > VEL: ship.x -= VEL
    if pressed_keys[pg.K_d] and ship.x + VEL < BORDER.x - ship.width: ship.x += VEL
    if pressed_keys[pg.K_s] and ship.y + VEL + ship.height < HEIGHT: ship.y += VEL
    if pressed_keys[pg.K_w] and ship.y > VEL: ship.y -= VEL


def move_ship_2(pressed_keys, ship):
    if pressed_keys[pg.K_LEFT] and ship.x > VEL + BORDER.x + BORDER.width: ship.x -= VEL
    if pressed_keys[pg.K_RIGHT] and ship.x + ship.width + VEL < WIDTH: ship.x += VEL
    if pressed_keys[pg.K_DOWN] and ship.y + VEL + ship.height < HEIGHT: ship.y += VEL
    if pressed_keys[pg.K_UP] and ship.y > VEL: ship.y -= VEL


def main():
    clock = pg.time.Clock()

    rec_1 = pg.Rect(.15*WIDTH, HEIGHT/2.2, S_WIDTH, S_HEIGHT)
    rec_2 = pg.Rect(.85*WIDTH, HEIGHT/2.2, S_WIDTH, S_HEIGHT)

    while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT: return pg.quit()
        
        init_window(rec_1, rec_2)
        pressed_keys = pg.key.get_pressed()
        move_ship_1(pressed_keys, rec_1)
        move_ship_2(pressed_keys, rec_2)


if __name__ == '__main__':
    main()