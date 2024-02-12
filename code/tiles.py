import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, path):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = (x, y))

class MapTiles(Tile):
    def __init__(self, x, y, path):
        super().__init__(x, y, path)
        self.is_flipped = False
        self.front = pygame.image.load(path)

        if self.is_flipped:
            self.image = pygame.image.load(path)
        else:
            self.image = pygame.image.load('graphics/card_back.png')

    def flip(self):
        self.image = self.front
        self.is_flipped = True

class RiverTiles(Tile):
    def __init__(self, x, y, path):
        super().__init__(x, y, path)
        self.image = pygame.image.load(path)