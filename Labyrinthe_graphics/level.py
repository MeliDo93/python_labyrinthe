import pygame
from os import path
from setting import *
from support import import_csv_layout
from game_data import img_folder
from tile import StaticTile


class level:
    def_init_(self, level_number, surface)
    self.dislay_surface = surface
    self.level_number = level_number

    # chargement des graphismes du Labyrinthe
    wall_level_file = path.join(path.dirname(__file__), 'level/Level_'str(lvel_number)+'Wall.csv')
    layout_wall = import_csv_layout(wall_level_file)
    self.wall_sprite = self.create_tile_group(layout_wall, 'wall')

    def create_tile_group(self, layout, name):
        sprite_groupe = pygame.sprite.Group()

        for row index, row in enumerate(layout):
            for col index, val in enumerate(row):
            if val != '-1':
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if name == 'wall':
                    img_name = 'wall_{}.png'.format(int(val)+1)
                    img_path = path.join(img_file['wall'], img_name)
                    sprite = StaticTile(TILE_SIZE, x, y, img_path)

                sprite_group.add(sprite)

        return sprite_group

    def run(self):
        # Wall
        self.wall_sprites.update()
        self.wall_sprites.draw(self.display_surface)
