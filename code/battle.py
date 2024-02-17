import pygame
import random
import sys

TURN_DELAY = 2000


class Abilities(pygame.sprite.Sprite):
    def __init__(self, pos, sprites, damage, is_player):
        super().__init__()

        self.sprites = sprites
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = damage
        self.is_player = is_player

    def update(self):
        self.current_sprite += 0.5
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


class BattleCard(pygame.sprite.Sprite):
    def __init__(self, pos, path, max_hp, alive, ability_sprites, is_player, shown_turn):
        super().__init__()

        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = pos)

        self.max_hp = max_hp
        self.current_hp = max_hp

        self.alive = alive
        self.ability_sprites = ability_sprites
        self.is_player = is_player
        self.shown_turn = shown_turn
        self.original_image = pygame.image.load(path)
    
    def show_turn(self):
        if not self.shown_turn:
            self.rect.x -= 10
            self.rect.y -= 10
            self.image = pygame.transform.scale(self.image, (self.rect.width + 20, self.rect.height + 20))
            self.shown_turn = True
    
    def end_turn(self):
        if self.shown_turn:
            self.rect.x += 10
            self.rect.y += 10
            self.image = self.original_image
            self.shown_turn = False

    def attack(self, target, ability):
        damage = random.randint(0, ability.damage)
        target.current_hp -= damage
        if target.current_hp < 1:
            target.current_hp = 0
            target.alive = False
        elif target.current_hp > target.max_hp:
            target.current_hp = target.max_hp


class Battle:
    def __init__(self, surface, sprites):
        self.display_surface = surface
        self.sprites = sprites

    def run(self):
        background = pygame.image.load('graphics/background.png')
        self.display_surface.blit(background, (0, 0))
        self.sprites.draw(self.display_surface)

        for sprite in self.sprites:
            if sprite.is_player:
                sprite.ability_sprites.draw(self.display_surface)
                sprite.ability_sprites.update()
            
        pygame.display.flip()