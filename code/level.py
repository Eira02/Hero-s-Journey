import pygame
from support import import_csv_layout
from tiles import Tile, MapTiles


class Level:
    def __init__(self, level_data, surface):
        # general setup
        self.display_surface = surface

        # cards setup
        forest_layout = import_csv_layout(level_data['card_front_forest'])
        self.forest_sprites = self.create_tile_group(forest_layout, 'card_front_forest')

        meadow_layout = import_csv_layout(level_data['card_front_meadow'])
        self.meadow_sprites = self.create_tile_group(meadow_layout, 'card_front_meadow')

        path_layout = import_csv_layout(level_data['card_front_path'])
        self.path_sprites = self.create_tile_group(path_layout, 'card_front_path')

        river_layout = import_csv_layout(level_data['card_front_river'])
        self.river_sprites = self.create_tile_group(river_layout, 'card_front_river')

    def create_tile_group(self, layout, type):
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
        # run the entire level
        background = pygame.image.load('graphics/background.png')
        self.display_surface.blit(background, (0, 0))

        self.forest_sprites.draw(self.display_surface)
        self.meadow_sprites.draw(self.display_surface)
        self.path_sprites.draw(self.display_surface)
        self.river_sprites.draw(self.display_surface)