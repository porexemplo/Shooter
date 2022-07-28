from turtle import back
import pygame as pg
from screeninfo import get_monitors
import os


WIDTH = .6*get_monitors()[0].width
HEIGHT = .6*get_monitors()[0].height

S_WIDTH = .08*HEIGHT
S_HEIGHT = .07*HEIGHT

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

BORDER = pg.Rect(WIDTH/2 - .005*WIDTH , 0, .01*WIDTH, HEIGHT)

BACKGROUND = pg.image.load(os.path.join('assets', 'background.png'))
BACKGROUND = pg.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

SHIP_1_HIT = pg.USEREVENT + 1
SHIP_2_HIT = pg.USEREVENT + 2

FPS = 60
VEL = .009*WIDTH
BULLET_VEL = 1.5*VEL
MAX_BULLETS = 4

def init_window(rec_1, rec_2, bullet_1, bullet_2):
    pg.display.set_caption('Shooter Game')
    SCREEN.blit(BACKGROUND, (0, 0))
    pg.draw.rect(SCREEN, (0, 0, 0), BORDER)
    SCREEN.blit(get_ship(1), (rec_1.x, rec_1.y))
    SCREEN.blit(get_ship(2), (rec_2.x, rec_2.y))

    # Drawing bullets
    for bullet in bullet_1 + bullet_2:
        pg.draw.rect(SCREEN, (255, 206, 36), bullet)

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


def handle_bullets(bullet_1, bullet_2, rec_1, rec_2):
    for bullet in bullet_1:
        bullet.x += BULLET_VEL
        if rec_2.colliderect(bullet):
            pg.event.post(pg.event.Event(SHIP_1_HIT))
            bullet_1.remove(bullet)
            return
        if bullet.x > WIDTH: bullet_1.remove(bullet)
    
    for bullet in bullet_2:
        bullet.x -= BULLET_VEL
        if rec_1.colliderect(bullet):
            pg.event.post(pg.event.Event(SHIP_2_HIT))
            bullet_2.remove(bullet)
            return
        if bullet.x + bullet.width < 0: bullet_2.remove(bullet)


def main():
    clock = pg.time.Clock()

    rec_1 = pg.Rect(.15*WIDTH, HEIGHT/2.2, S_WIDTH, S_HEIGHT)
    rec_2 = pg.Rect(.85*WIDTH, HEIGHT/2.2, S_WIDTH, S_HEIGHT)

    bullet_1, bullet_2 = list(), list()

    while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT: return pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_v and len(bullet_1) < MAX_BULLETS:
                    bullet = pg.Rect(
                                     rec_1.x + rec_1.width,
                                     rec_1.y + rec_1.height/2 - .004*HEIGHT,
                                     .01*WIDTH,
                                     .007*HEIGHT
                                    )
                    bullet_1.append(bullet)
                if event.key == pg.K_b and len(bullet_2) < MAX_BULLETS:
                    bullet = pg.Rect(
                                     rec_2.x,
                                     rec_2.y + rec_2.height/2 - .004*HEIGHT,
                                     .01*WIDTH,
                                     .007*HEIGHT
                                    )
                    bullet_2.append(bullet)
        
        init_window(rec_1, rec_2, bullet_1, bullet_2)
        handle_bullets(bullet_1, bullet_2, rec_1, rec_2)
        pressed_keys = pg.key.get_pressed()
        move_ship_1(pressed_keys, rec_1)
        move_ship_2(pressed_keys, rec_2)


if __name__ == '__main__':
    main()