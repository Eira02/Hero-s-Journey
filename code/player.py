import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/player.png')
        self.rect = self.image.get_rect(center = (x , y))

    def update_position(self, pos):
        self.rect.center = pos