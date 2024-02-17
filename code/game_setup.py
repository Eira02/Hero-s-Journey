import pygame
from settings import *
from player import Player
from level import Level
from game_data import level_0
from battle import *

screen = pygame.display.set_mode((screen_width, screen_height))

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


sword_sprites = []
sword_sprites.append(pygame.image.load('graphics/sword_animation_1.png'))
sword_sprites.append(pygame.image.load('graphics/sword_animation_2.png'))
sword_sprites.append(pygame.image.load('graphics/sword_animation_3.png'))
sword_sprites.append(pygame.image.load('graphics/sword_animation_4.png'))
sword_sprites.append(pygame.image.load('graphics/sword_animation_5.png'))
sword_sprites.append(pygame.image.load('graphics/sword_animation_6.png'))
sword_sprites.append(pygame.image.load('graphics/sword_animation_7.png'))

fire_sprites = []
fire_sprites.append(pygame.image.load('graphics/fire_animation_1.png'))
fire_sprites.append(pygame.image.load('graphics/fire_animation_2.png'))
fire_sprites.append(pygame.image.load('graphics/fire_animation_3.png'))
fire_sprites.append(pygame.image.load('graphics/fire_animation_4.png'))
fire_sprites.append(pygame.image.load('graphics/fire_animation_5.png'))
fire_sprites.append(pygame.image.load('graphics/fire_animation_6.png'))
fire_sprites.append(pygame.image.load('graphics/fire_animation_7.png'))
fire_sprites.append(pygame.image.load('graphics/fire_animation_8.png'))
fire_sprites.append(pygame.image.load('graphics/fire_animation_9.png'))

heal_sprites = []
heal_sprites.append(pygame.image.load('graphics/heal_animation_1.png'))
heal_sprites.append(pygame.image.load('graphics/heal_animation_2.png'))
heal_sprites.append(pygame.image.load('graphics/heal_animation_3.png'))
heal_sprites.append(pygame.image.load('graphics/heal_animation_4.png'))
heal_sprites.append(pygame.image.load('graphics/heal_animation_5.png'))
heal_sprites.append(pygame.image.load('graphics/heal_animation_6.png'))
heal_sprites.append(pygame.image.load('graphics/heal_animation_7.png'))
heal_sprites.append(pygame.image.load('graphics/heal_animation_8.png'))
heal_sprites.append(pygame.image.load('graphics/heal_animation_9.png'))

sword_attack = Abilities((600, 400), sword_sprites, 3, True)
fire_attack = Abilities((800, 400), fire_sprites, 3, False)
heal_spell = Abilities((1000, 400), heal_sprites, -3, False)

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