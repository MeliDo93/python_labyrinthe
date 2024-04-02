import pygame


class StaticTile(pygame.sprite.Sprite):
    def __init__(self, size, x, y, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
