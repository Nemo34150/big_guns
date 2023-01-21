import pygame


# класс взрыва
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.i = 0
        self.x = x
        self.y = y
        self.list_animation = []
        self.list_animation.append(pygame.image.load('explosion_1.png'))
        self.list_animation.append(pygame.image.load('explosion_2.png'))
        self.list_animation.append(pygame.image.load('explosion_3.png'))
        self.list_animation.append(pygame.image.load('explosion_4.png'))
        self.list_animation.append(pygame.image.load('explosion_5.png'))
        self.image = self.list_animation[self.i]
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self, *args):
        self.i += 1
        if self.i >= len(self.list_animation):
            pass
            if self.i > 15:
                self.kill()
        else:
            self.image = self.list_animation[self.i]
            self.rect = self.image.get_rect(center=(self.x, self.y))
