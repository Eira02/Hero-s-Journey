import pygame
from support import import_csv_layout
from tiles import Tile, MapTiles


class Level:
    """
    Class representing a game level.

    Attributes:
        display_surface (pygame.Surface): The surface to display the level on.
        forest_sprites (pygame.sprite.Group): Sprite group for forest tiles.
        meadow_sprites (pygame.sprite.Group): Sprite group for meadow tiles.
        path_sprites (pygame.sprite.Group): Sprite group for path tiles.
        river_sprites (pygame.sprite.Group): Sprite group for river tiles.
    """

    def __init__(self, level_data, surface):
        """
        Initializes the level with the given data.

        Args:
            level_data (dict): A dictionary containing level data.
            surface (pygame.Surface): The surface to display the level on.
        """
        self.display_surface = surface

        forest_layout = import_csv_layout(level_data['card_front_forest'])
        self.forest_sprites = self.create_tile_group(forest_layout, 'card_front_forest')

        meadow_layout = import_csv_layout(level_data['card_front_meadow'])
        self.meadow_sprites = self.create_tile_group(meadow_layout, 'card_front_meadow')

        path_layout = import_csv_layout(level_data['card_front_path'])
        self.path_sprites = self.create_tile_group(path_layout, 'card_front_path')

        river_layout = import_csv_layout(level_data['card_front_river'])
        self.river_sprites = self.create_tile_group(river_layout, 'card_front_river')

    def create_tile_group(self, layout, type):
        """
        Creates a group of tiles based on the provided layout and type.

        Args:
            layout (list): A 2D list representing the tile layout.
            type (str): The type of tiles to create.

        Returns:
            pygame.sprite.Group: A sprite group containing the created tiles.
        """
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                if value != '-1':
                    x = (col_index * 106) + 6
                    y = (row_index * 154) + 6

                    if type == 'card_front_forest':
                        sprite = MapTiles(x, y, 'graphics/card_front_forest.png')
                        sprite_group.add(sprite)

                    if type == 'card_front_meadow':
                        sprite = MapTiles(x, y, 'graphics/card_front_meadow.png')
                        sprite_group.add(sprite)

                    if type == 'card_front_path':
                        sprite = MapTiles(x, y, 'graphics/card_front_path.png')
                        sprite_group.add(sprite)

                    if type == 'card_front_river':
                        sprite = Tile(x, y, 'graphics/card_front_river.png')
                        sprite_group.add(sprite)

        return sprite_group

    def run(self):
        """Runs the entire level, displaying all tiles on the screen."""
        background = pygame.image.load('graphics/background.png')
        self.display_surface.blit(background, (0, 0))

        self.forest_sprites.draw(self.display_surface)
        self.meadow_sprites.draw(self.display_surface)
        self.path_sprites.draw(self.display_surface)
        self.river_sprites.draw(self.display_surface)