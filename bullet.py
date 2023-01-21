import pygame


# класс пули
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_p, y_p, speed):
        pygame.sprite.Sprite.__init__(self)
        # позиция
        self.x = x_p
        self.y = y_p
        # скорость
        self.speed = speed
        self.image = pygame.image.load('bullet1.png').convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        if self.rect.y < 0:
            self.kill()
        else:
            self.rect.y -= self.speed
