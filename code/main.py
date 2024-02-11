import pygame
from sys import exit
from level import Level
from game_data import level_0

pygame.init()
screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)
pygame.display.set_caption("Hero's Journey")
level = Level(level_0, screen)

background = pygame.image.load('../graphics/background.png')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for tile in level.forest_sprites:
                tile.flip(mouse_pos)

            for tile in level.meadow_sprites:
                tile.flip(mouse_pos)

            for tile in level.path_sprites:
                tile.flip(mouse_pos)

        
    screen.blit(background, (0, 0))
    
    level.run()
    
    pygame.display.update()
    clock.tick(60)