import pygame


# класс персонажа
class Hero:
    def __init__(self, name_animation_stop, name_animation_left, name_animation_right, x, y, speed):
        # координаты
        self.x = x
        self.y = y
        # скорость
        self.speed = speed

        self.animation_stop = pygame.image.load(name_animation_stop)
        self.animation_left = pygame.image.load(name_animation_left)
        self.animation_right = pygame.image.load(name_animation_right)
        self.rect = self.animation_stop.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.animation_stop)
