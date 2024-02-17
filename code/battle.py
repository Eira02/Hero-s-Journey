import pygame
import random
import sys

TURN_DELAY = 2000


class Abilities(pygame.sprite.Sprite):
    """
    A class representing abilities of characters.

    Attributes:
        pos (tuple): The position of the ability on the screen.
        sprites (list): List of images representing the ability.
        damage (int): The damage caused by the ability.
    """
     
    def __init__(self, pos, sprites, damage):
        super().__init__()

        self.sprites = sprites
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = damage

    def update(self):
        """Update method to cycle through ability sprites."""
        self.current_sprite += 0.5
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


class BattleCard(pygame.sprite.Sprite):
    """
    A class representing a character battle card.

    Attributes:
        pos (tuple): The position of the character on the screen.
        path (str): The file path to the character's image.
        max_hp (int): The maximum health points of the character.
        alive (bool): Indicates whether the character is alive.
        ability_sprites (pygame.sprite.Group): Group containing ability sprites associated with the character.
        is_player (bool): Indicates whether the character is the player or enemy.
        shown_turn (bool): Indicates whether it's the character's turn and the turn is shown.
        original_image (pygame.Surface): The original image of the character.
    """

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
        """Show the turn of the character by scaling its image and adjusting position."""
        if not self.shown_turn:
            self.rect.x -= 10
            self.rect.y -= 10
            self.image = pygame.transform.scale(self.image, (self.rect.width + 20, self.rect.height + 20))
            self.shown_turn = True
    
    def end_turn(self):
        """End the turn of the character by restoring its original image and position."""
        if self.shown_turn:
            self.rect.x += 10
            self.rect.y += 10
            self.image = self.original_image
            self.shown_turn = False

    def attack(self, target, ability):
        """
        Perform an attack on the target character using a given ability.

        Args:
            target (BattleCard): The target character of the attack.
            ability (Abilities): The ability used for the attack.
        """
        damage = random.randint(0, ability.damage)
        target.current_hp -= damage
        if target.current_hp < 1:
            target.current_hp = 0
            target.alive = False
        elif target.current_hp > target.max_hp:
            target.current_hp = target.max_hp


class Battle:
    """
    A class representing a battle sequence.

    Attributes:
        surface (pygame.Surface): The display surface where the battle is rendered.
        sprites (pygame.sprite.Group): Group containing all sprites involved in the battle.
    """

    def __init__(self, surface, sprites):
        """
        Initialize the Battle object.

        Args:
            surface (pygame.Surface): The display surface where the battle is rendered.
            sprites (pygame.sprite.Group): Group containing all sprites involved in the battle.
        """
        self.display_surface = surface
        self.sprites = sprites

    def run(self):
        """Renders the battle sequence."""
        background = pygame.image.load('graphics/background.png')
        self.display_surface.blit(background, (0, 0))
        self.sprites.draw(self.display_surface)

        for sprite in self.sprites:
            if sprite.is_player:
                sprite.ability_sprites.draw(self.display_surface)
                sprite.ability_sprites.update()
            
        pygame.display.flip()