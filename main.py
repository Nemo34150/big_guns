# импорт библиотек
import pygame
from explosion import Explosion
from hero import Hero
from bullet import Bullet

res = open('res.txt', 'r')
res_list = res.read().split('\n')
res.close()
meteorites = pygame.sprite.Group()
explosions = pygame.sprite.Group()
bullets = pygame.sprite.Group()

flag_level = 0
flag_win = False
count_level = 20
wait_level = 100
running = True
flag_live = True
flag_end = False
time = 0
speed_meteorite_big = 1
speed_meteorite_small = 3
speed_meteorite_fast = 5

pygame.init()
# настройки экрана
w = 360
h = 480
screen = pygame.display.set_mode((w, h))


# враг
class Enemy:
    def __init__(self, x_p, y_p, hp):
        self.x = x_p
        self.y = y_p
        self.hp = hp


# метеориты
class Meteorite(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, s):
        self.x = x
        self.y = y
        # наследование от класса спрайт
        pygame.sprite.Sprite.__init__(self)
        # загружаем изображения
        self.image = pygame.image.load(filename).convert_alpha()
        # прямоугольник для столкновений
        self.h = self.image.get_height()
        self.w = self.image.get_width()
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = s

    # изменение позиции метеорита
    def update(self, hero_1, *args):
        global running
        global flag_live
        global flag_end
        if self.rect.y < h - 20:
            self.rect.y += self.speed
        else:
            # исключение из всех групп спрайтов
            self.kill()
        if pygame.sprite.collide_mask(self, hero_1):
            explosions.add(Explosion(hero_1.rect.x + 22, hero_1.rect.y + 20))
            self.kill()
            flag_live = False
            flag_end = True


def e_level_1(hero):
    meteorites.add(Meteorite(w // 2 - 100, -200, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -250, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -350, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 100, -400, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 150, -450, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -500, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 + 100, -600, 'rock3.png', speed_meteorite_fast),)
    meteorites.add(Meteorite(w // 2 + 100, -800, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -250, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -350, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 100, -400, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 150, -450, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -500, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 + 100, -600, 'rock3.png', speed_meteorite_fast),)


def level_1_update(hero):
    global wait_level
    global count_level
    if wait_level == 0:
        if count_level != 0:
            meteorites.add(Meteorite(hero.rect.x, -200, 'rock3.png', speed_meteorite_fast))
            meteorites.add(Meteorite(hero.rect.x - 100, -200, 'rock3.png', speed_meteorite_fast),
                           Meteorite(hero.rect.x - 150, -250, 'rock3.png', speed_meteorite_fast),
                           Meteorite(hero.rect.x + 50, -350, 'rock3.png', speed_meteorite_fast),
                           Meteorite(hero.rect.x + 100, -400, 'rock3.png', speed_meteorite_fast),
                           Meteorite(hero.rect.x - 50, -450, 'rock3.png', speed_meteorite_fast),
                           Meteorite(w // 2, -500, 'rock3.png', speed_meteorite_fast))
            wait_level = 100
            count_level -= 1
    else:
        wait_level -= 1


def e_level_2():
    # уровень 1
    # создаём метеориты
    meteorites.add(Meteorite(w // 2 - 100, -200, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -250, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -350, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 100, -400, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 150, -450, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -500, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 + 100, -600, 'rock3.png', speed_meteorite_fast),)
    # волна 1
    meteorites.add(Meteorite(w // 2, -700, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 + 100, -900, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -950, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 + 50, -1000, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 50, -1000, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 100, -1000, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 150, -1000, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 + 150, -1000, 'rock3.png', speed_meteorite_fast))

    meteorites.add(Meteorite(w // 2 + 100, -1700, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -1150, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -1250, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 100, -1300, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 150, -1350, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -1400, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 + 100, -1500, 'rock3.png', speed_meteorite_fast),)
    # волна 2
    meteorites.add(Meteorite(w // 2, -1700, 'rock4.png', speed_meteorite_small),
                   Meteorite(w // 2 - 50, -1650, 'rock2.png', speed_meteorite_small),
                   Meteorite(w // 2 + 50, -1650, 'rock4.png', speed_meteorite_small),
                   Meteorite(w // 2 + 150, -1650, 'rock4.png', speed_meteorite_small),
                   Meteorite(w // 2 + 100, -1700, 'rock2.png', speed_meteorite_small),
                   Meteorite(w // 2 - 100, -1700, 'rock4.png', speed_meteorite_small),
                   Meteorite(w // 2 - 150, -1600, 'rock2.png', speed_meteorite_small))

    meteorites.add(Meteorite(w // 2 - 100, -1800, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -1850, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -1950, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 100, -2000, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 - 150, -2050, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2, -2100, 'rock3.png', speed_meteorite_fast),
                   Meteorite(w // 2 + 100, -2200, 'rock3.png', speed_meteorite_fast),)
    # волна 3
    meteorites.add(Meteorite(w // 2 - 150, -2300, 'rock4.png', speed_meteorite_small),
                   Meteorite(w // 2 - 100, -2350, 'rock2.png', speed_meteorite_small),
                   Meteorite(w // 2 - 50, -2400, 'rock4.png', speed_meteorite_small),
                   Meteorite(w // 2 - 50, -2450, 'rock2.png', speed_meteorite_small),
                   Meteorite(w // 2 - 50, -2550, 'rock4.png', speed_meteorite_small),
                   Meteorite(w // 2, -2550, 'rock2.png', speed_meteorite_small),
                   Meteorite(w // 2 + 50, -2550, 'rock4.png', speed_meteorite_small),
                   Meteorite(w // 2 + 50, -2500, 'rock2.png', speed_meteorite_small),
                   Meteorite(w // 2 + 50, -2450, 'rock4.png', speed_meteorite_small),
                   Meteorite(w // 2 + 100, -2400, 'rock2.png', speed_meteorite_small))

    # волна 4
    meteorites.add(Meteorite(w // 2, -900, 'rock1.png', speed_meteorite_big),
                   Meteorite(w // 2 + 130, -900, 'rock1.png', speed_meteorite_big),
                   Meteorite(w // 2 - 130, -900, 'rock1.png', speed_meteorite_big),
                   Meteorite(w // 2 + 55, -1100, 'rock1.png', speed_meteorite_big),
                   Meteorite(w // 2 - 55, -1100, 'rock1.png', speed_meteorite_big),
                   Meteorite(w // 2 - 155, -1100, 'rock1.png', speed_meteorite_big),
                   Meteorite(w // 2, -1200, 'rock1.png', speed_meteorite_big),
                   Meteorite(w // 2 + 130, -1200, 'rock1.png', speed_meteorite_big),
                   Meteorite(w // 2 - 130, -1200, 'rock1.png', speed_meteorite_big), )


def start():
    # инициализация библиотеки

    pygame.display.set_caption('Big guns')

    fon = pygame.image.load('fon.png').convert_alpha()
    button_start = pygame.image.load('start.png').convert_alpha()
    hero_block = pygame.image.load('ship.png').convert_alpha()

    clock = pygame.time.Clock()
    fps = 60

    running = True

    while running:
        # проверка нажатий кнопок игрока
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'none'
            # нажатия на кнопки
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 0 < event.pos[0] < 360 and 100 < event.pos[1] < 221:
                    return 'level_menu'

        screen.blit(fon, (0, 0))
        screen.blit(button_start, (-25, 100))
        screen.blit(hero_block, (w // 2 - 25, 300))
        # для оптимизации нагрузки и контроля игрового времени
        clock.tick(fps)
        # для отображения
        pygame.display.flip()
    pygame.quit()


def game():
    global count_level
    global running
    global time
    global flag_live
    global flag_end
    global res_list
    global name_com

    flag_live = True
    time = 0
    flag_end = False

    # инициализация библиотеки

    pygame.display.set_caption('Big guns')

    # загрузка изображений
    fon = pygame.image.load('fon.png').convert_alpha()
    enemy_image = pygame.image.load('enemy1.png').convert_alpha()

    # переменная для контроля игрового времени
    clock = pygame.time.Clock()
    fps = 60

    speed_hero = 5

    hero_x = w // 2
    hero_y = 300
    enemy = []
    bullet = []

    meteorites.empty()
    bullets.empty()
    explosions.empty()

    hero = Hero('ship.png', 'ship_left.png', 'ship_right.png', hero_x, hero_y, speed_hero)
    count_level = 20
    if flag_level == 2:
        e_level_2()
    elif flag_level == 1:
        e_level_1(hero)

    # главный цикл
    while running:
        # проверка нажатий кнопок игрока
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'none'
            # стрельба
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullets.add(Bullet(hero.rect.x + 22, hero.rect.y, 5))

        # анимация при остановке
        hero_image = hero.animation_stop
        # управление
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if hero.rect.x > 0:
                hero.rect.x -= hero.speed
                hero_image = hero.animation_left
        if keys[pygame.K_RIGHT]:
            if hero.rect.x < 320:
                hero.rect.x += hero.speed
                hero_image = hero.animation_right
        if keys[pygame.K_UP]:
            hero.rect.y -= hero.speed
        if keys[pygame.K_DOWN]:
            if hero.rect.y < 440:
                hero.rect.y += hero.speed

        # очистка экрана
        # фон
        screen.blit(fon, (0, 0))
        # работа с пулями
        bullets.draw(screen)
        bullets.update()
        # отрисовка всех объектов
        if len(meteorites) == 0:
            if flag_live:
                if flag_level == 1:
                    res_list[0] = 'True'
                    return 'level_menu'
                elif flag_level == 2:
                    res_list[1] = 'True'
                    return 'level_menu'
        if flag_end:
            time += 1
            if time == 30:
                return 'level_menu'
        if flag_live:
            screen.blit(hero_image, (hero.rect.x, hero.rect.y))

        meteorites.draw(screen)
        explosions.draw(screen)
        explosions.update()

        meteorites.update(hero)
        if flag_level == 1:
            level_1_update(hero)

        # для оптимизации нагрузки и контроля игрового времени
        clock.tick(fps)
        # для отображения
        pygame.display.flip()


def level_menu():
    global flag_win
    # инициализация библиотеки

    pygame.display.set_caption('Big guns')

    if res_list[0] == 'True' and res_list[1] == 'True':
        flag_win = True

    fon = pygame.image.load('fon.png').convert_alpha()
    level_but = pygame.image.load('table.png').convert_alpha()
    win_but = pygame.transform.scale(level_but, (110, 100))
    star_01 = pygame.image.load('star_01.png').convert_alpha()
    star_1 = pygame.transform.scale(star_01, (100, 100))
    star_02 = pygame.image.load('star_02.png').convert_alpha()
    star_2 = pygame.transform.scale(star_02, (100, 100))
    f1 = pygame.font.Font(None, 100)
    text1 = f1.render('Level 1', True, (255, 255, 255))
    text2 = f1.render('Level 2', True, (255, 255, 255))

    f2 = pygame.font.Font(None, 44)
    text_win = f2.render('Финал', True, (255, 255, 255))

    clock = pygame.time.Clock()
    fps = 60

    while True:
        # проверка нажатий кнопок игрока
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'none'
            # нажатия на кнопки
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 0 < event.pos[0] < 360 and 20 < event.pos[1] < 121:
                    return 'game 1'
                elif 0 < event.pos[0] < 360 and 220 < event.pos[1] < 321:
                    return 'game 2'
                elif flag_win and 245 < event.pos[0] < 345 and 360 < event.pos[1] < 460:
                    return 'final'

        screen.blit(fon, (0, 0))

        screen.blit(level_but, (0, 20))
        screen.blit(text1, (60, 30))
        if res_list[0] == 'True':
            screen.blit(star_2, (125, 115))
        else:
            screen.blit(star_1, (125, 115))

        screen.blit(level_but, (0, 220))
        screen.blit(text2, (60, 230))
        if res_list[1] == 'True':
            screen.blit(star_2, (125, 315))
        else:
            screen.blit(star_1, (125, 315))

        if flag_win:
            screen.blit(win_but, (245, 360))
            screen.blit(text_win, (250, 385))

        # для оптимизации нагрузки и контроля игрового времени
        clock.tick(fps)
        # для отображения
        pygame.display.flip()


def final():
    pygame.display.set_caption('Big guns')

    fon = pygame.image.load('fon.png').convert_alpha()

    f2 = pygame.font.Font(None, 40)
    s1 = 'Над игрой работали'
    s2 = 'Геймдизайнер - алкаш'
    s3 = 'Художник украл планшет и сбежал'
    s4 = 'Программист вообще '
    s5 = 'не работал'
    s6 = 'Спасибо за игру'
    text1 = f2.render(s1, True, (255, 255, 255))
    text2 = f2.render(s2, True, (255, 255, 255))
    text3 = f2.render(s3, True, (255, 255, 255))
    text4 = f2.render(s4, True, (255, 255, 255))
    text5 = f2.render(s5, True, (255, 255, 255))
    text6 = f2.render(s6, True, (255, 255, 255))

    clock = pygame.time.Clock()
    fps = 60

    while True:
        # проверка нажатий кнопок игрока
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'none'

        screen.blit(fon, (0, 0))
        screen.blit(text1, (30, 0))
        screen.blit(text2, (10, 50))
        screen.blit(text3, (10, 100))
        screen.blit(text4, (10, 150))
        screen.blit(text5, (10, 200))
        screen.blit(text6, (30, 250))
        # для оптимизации нагрузки и контроля игрового времени
        clock.tick(fps)
        # для отображения
        pygame.display.flip()


name_com = 'start'
while True:
    if name_com == 'start':
        name_com = start()
    elif name_com == 'none':
        res = open('res.txt', 'w')
        res.write(f'{res_list[0]}\n{res_list[1]}')
        res.close()
        break
    elif name_com == 'level_menu':
        name_com = level_menu()
    elif name_com == 'game 1':
        flag_level = 1
        name_com = game()
    elif name_com == 'game 2':
        flag_level = 2
        name_com = game()
    elif name_com == 'final':
        name_com = final()
