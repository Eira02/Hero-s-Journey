import pygame
from sys import exit
from settings import starting_player_pos
from game_data import level_0
from player import Player, keyboard_camera_control
from level import Level

pygame.init()

screen = pygame.display.set_mode((1500, 700), pygame.RESIZABLE)
pygame.display.set_caption("Hero's Journey")

background = pygame.image.load('graphics/background.png')

player_sprite = Player(starting_player_pos)
player_list = pygame.sprite.Group()
player_list.add(player_sprite)

level = Level(level_0, screen)
all_level_sprites = pygame.sprite.Group()
all_level_sprites.add(
    level.forest_sprites, level.meadow_sprites,
    level.path_sprites, level.river_sprites
)

all_sprites = pygame.sprite.Group()
all_sprites.add(
    level.forest_sprites, level.meadow_sprites,
    level.path_sprites, level.river_sprites, player_sprite
)

player_sprite.focus_camera(screen, all_sprites)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            player_sprite.center_player(all_level_sprites, mouse_pos)

    keyboard_camera_control(all_sprites)
    screen.blit(background, (0, 0))
    level.run()
    player_list.draw(screen)

    collisions = pygame.sprite.spritecollide(player_sprite, all_level_sprites, False)
    for tile in collisions:
        if not tile.is_flipped:
            tile.flip()

    pygame.display.update()
    clock.tick(60)