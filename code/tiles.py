import pygame


class Tile(pygame.sprite.Sprite):
    """
    A class representing a tile in the level state of game.

    Attributes:
        x (int): The x-coordinate of the tile's top-left corner.
        y (int): The y-coordinate of the tile's top-left corner.
        path (str): The file path to the image of the tile.
        image (pygame.Surface): The image of the tile.
        rect (pygame.Rect): The rectangular area of the tile.
        is_flipped (bool): Flag indicating whether the tile is flipped.
    """

    def __init__(self, x, y, path):
        """
        Initialize the Tile object.

        Args:
            x (int): The x-coordinate of the tile's top-left corner.
            y (int): The y-coordinate of the tile's top-left corner.
            path (str): The file path to the image of the tile.
        """
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = (x, y))
        self.is_flipped = False

    def flip(self):
        """Function used by the tiles that are always flipped. (River Tiles)"""
        pass


class MapTiles(Tile):
    """
    A subclass of Tile representing tiles on which the player can move.

    Attributes:
        front (pygame.Surface): The image of the tile when it's flipped.
    """
     
    def __init__(self, x, y, path):
        """
        Initialize the MapTiles object.

        Args:
            x (int): The x-coordinate of the tile's top-left corner.
            y (int): The y-coordinate of the tile's top-left corner.
            path (str): The file path to the image of the tile.
        """
        super().__init__(x, y, path)
        self.front = pygame.image.load(path)

        if self.is_flipped:
            self.image = pygame.image.load(path)
        else:
            self.image = pygame.image.load('graphics/card_back.png')

    def flip(self):
        """Flip the tile to reveal its front image."""
        self.image = self.front
        self.is_flipped = True