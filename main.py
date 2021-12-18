# -*- coding: utf-8 -*-
from Camera import *
from object import *
from projection import *


class Render:
    u"""
    Стандартный класс программы, отвечающий за создания тела программы
    """

    def __init__(self):
        u"""
        Функция инициализации стандартных для pygame переменных
        wight и hight - разрешение
        HfWidth и HfHeight - видимость камеры
        screen - экран
        camera - камера
        font-задний план
        """
        pg.init()
        infoObject = pg.display.Info()
        self.width, self.height = infoObject.current_w, infoObject.current_h
        self.res = self.width, self.height
        self.HfWidth, self.HfHeight = self.width // 2, self.height // 2
        self.screen = pg.display.set_mode(self.res, pg.FULLSCREEN)
        self.FPS, self.clock = 60, pg.time.Clock()

        self.camera = Camera(self, [-0.5, 0.5, -4])
        self.projection = Projection_Matrix(self)
        self.objects = []
        self.objects.append(Object3d(self))

        self.font = pg.font.SysFont('Times New Roman', 16)
        self.font_color = (pg.Color('black'))
        self.font_background = (pg.Color('lightskyblue1'))

        pg.mouse.set_visible(True)
        pg.mouse.set_pos(self.HfWidth, self.HfHeight)

    def draw(self):
        u"""
        Класс для отрисовки объекта на экране
        """
        self.screen.fill(pg.Color('lightskyblue1'))
        for i in range(len(self.objects)):
            self.objects[i].update()

        x = self.font.render("x y " + str(pg.mouse.get_pos()[0]), True, self.font_color, self.font_background)
        y = self.font.render(str(pg.mouse.get_pos()[1]), True, self.font_color, self.font_background)
        FPS = self.font.render("FPS " + str(int(self.clock.get_fps())), True, self.font_color, self.font_background)
        x_rect, y_rect, FPS_rect = x.get_rect(), y.get_rect(), FPS.get_rect()
        x_rect.centerx, x_rect.centery = 30, 10
        y_rect.centerx, y_rect.centery = 75, 10
        FPS_rect.centerx, FPS_rect.centery = 25, 30
        self.screen.blit(x, x_rect)
        self.screen.blit(y, y_rect)
        self.screen.blit(FPS, FPS_rect)

    def run(self):
        u"""
        Функция, работающая при работе программы, которая двигает объект
        при нажатии на определенные клавиши
        """
        while True:
            self.draw()
            self.camera.control()
            events = pg.event.get()
            for i in events:
                if i.type == pg.KEYDOWN:
                    if i.key == pg.K_ESCAPE:
                        exit()

            x, y = pg.mouse.get_pos()
            if x < 10:
                pg.mouse.set_pos(self.width - 10, y)
            if x > self.width - 10:
                pg.mouse.set_pos(10, y)
            if y < 10:
                pg.mouse.set_pos(x, self.height - 10)
            if y > self.height - 10:
                pg.mouse.set_pos(x, 10)

            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    u"""
    Инициализация проекта
    """
    window = Render()
    window.run()

# main - 30
# object - 40
# camera - 67
# projection - 27
# matrix - 38
