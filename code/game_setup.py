import pygame
from settings import *
from player import Player
from level import Level
from game_data import level_0
from battle import *

screen = pygame.display.set_mode((screen_width, screen_height))

# Level sprites
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

# Battle sprites
sword_sprites = []
for i in range(1, 8):
    image_path = f'graphics/sword_animation_{i}.png'
    sword_sprites.append(pygame.image.load(image_path))

fire_sprites = []
for i in range(1, 10):
    image_path = f'graphics/fire_animation_{i}.png'
    fire_sprites.append(pygame.image.load(image_path))

heal_sprites = []
for i in range(1, 10):
    image_path = f'graphics/heal_animation_{i}.png'
    heal_sprites.append(pygame.image.load(image_path))

sword_attack = Abilities((600, 400), sword_sprites, 3)
fire_attack = Abilities((800, 400), fire_sprites, 3)
heal_spell = Abilities((1000, 400), heal_sprites, -3)

ability_sprites = pygame.sprite.Group()
ability_sprites.add(sword_attack, fire_attack, heal_spell)

player = BattleCard((400, 400), 'graphics/player_knight.png', 30, True, ability_sprites, True, False)
enemy_1 = BattleCard((600, 100), 'graphics/enemy_knight.png',  10, True, ability_sprites, False, False)
enemy_2 = BattleCard((800, 100), 'graphics/enemy_bunny.png', 15, True, ability_sprites, False, False)

characters = pygame.sprite.Group()
characters.add(player, enemy_1, enemy_2)

enemy_list = pygame.sprite.Group()
enemy_list.add(enemy_1, enemy_2)

initiate_battle = Battle(screen, characters)