import pygame
from sys import exit
from level import Level
from game_data import level_0
from player import Player

pygame.init()

screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)
background = pygame.image.load('graphics/background.png')
pygame.display.set_caption("Hero's Journey")

player_sprite = Player((3 * 106) + 57, (3 * 154) + 77)
player_list = pygame.sprite.Group()
player_list.add(player_sprite)

level = Level(level_0, screen)
all_level_sprites = pygame.sprite.Group()
all_level_sprites.add(level.forest_sprites, level.meadow_sprites, level.path_sprites)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for tile in all_level_sprites:
                if tile.rect.collidepoint(mouse_pos) and tile.is_flipped:
                    player_sprite.update_position(tile.rect.center) 
        
    screen.blit(background, (0, 0))
    level.run()

    player_list.draw(screen)

    collisions = pygame.sprite.spritecollide(player_sprite, all_level_sprites, False)
    for tile in collisions:
        if not tile.is_flipped:
            tile.flip()
    
    pygame.display.update()
    clock.tick(60)