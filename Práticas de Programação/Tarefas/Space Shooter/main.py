import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 640, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

#carregando as imagens

RED_SPACE_SHIP = pygame.image.load("pixel_ship_red_small.png")
GREEN_SPACE_SHIP = pygame.image.load("pixel_ship_green_small.png")
BLUE_SPACE_SHIP = pygame.image.load("pixel_ship_blue_small.png")

#player
YELLOW_SPACE_SHIP = pygame.image.load("pixel_ship_yellow.png")

#lasers
RED_LASER = pygame.image.load("pixel_laser_red.png")
GREEN_LASER = pygame.image.load("pixel_laser_green.png")
BLUE_LASER = pygame.image.load("pixel_laser_blue.png")
YELLOW_LASER = pygame.image.load("pixel_laser_yellow.png")

#fundo
BG = pygame.transform.scale(pygame.image.load("background-black.png"),(WIDTH, HEIGHT))

#criando as classes

class Ship():
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
            pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 20)

    ship = Ship(300, 450)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0,0))
        #desenhando o texto
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        ship.draw(WIN)
        
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            

main()

