# -*- coding: utf-8 -*-
import pygame as pg
from matrix import *


class Camera:
    u"""
    Класс, отвечающий за комеру
    """
    def __init__(self, render, cords):
        u"""
        Функция, в которой вводим начальную позицию камеры
        и векторы ориентации, области видимости
        render - 'отрисовка'
        position - координаты камеры
        close и far - ближняя и дальняя грани призмы проекции
        """
        self.render = render
        self.position = np.array([*cords, 1.0])
        self.pars = [(np.array([0, 0, 1, 1])),(np.array([0, 1, 0, 1])),(np.array([1, 0, 0, 1]))]
        self.screen_par = [(math.pi / 3), ((math.pi / 3) * (render.height / render.width))]
        self.close, self.far = 0.1, 100
        self.ms, self.rs = 0.1, 0.015

    def control(self):
        u"""
        Функция, которая в зависимости от нажатой кнопки перемещает камеру в пространстве
        """
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.position -= self.pars[2] * self.ms
        if key[pg.K_d]:
            self.position += self.pars[2] * self.ms
        if key[pg.K_w]:
            self.position += self.pars[0] * self.ms
        if key[pg.K_s]:
            self.position -= self.pars[0] * self.ms
        if key[pg.K_SPACE]:
            self.position += self.pars[1] * self.ms
        if key[pg.K_LSHIFT]:
            self.position -= self.pars[1] * self.ms

        if key[pg.K_LEFT]:
            self.rot_cam(-self.rs, 0)
        if key[pg.K_RIGHT]:
            self.rot_cam(self.rs, 0)
        if key[pg.K_UP]:
            self.rot_cam(-self.rs, 1)
        if key[pg.K_DOWN]:
            self.rot_cam(self.rs, 1)
        if key[pg.K_r]:
            self.position = np.array([-0.5, 0.5, -4, 1.0])
            self.pars[0], self.pars[1], self.pars[2] = np.array([0, 0, 1, 1]), np.array([0, 1, 0, 1]), np.array([1, 0, 0, 1])

    def rot_cam(self, angle, ch):
        u"""
        Функция, перемещающая камеру в начало координат
        (матрицы вращения)
        """
        if ch == 0:
            rot = rotate_around_y(angle)
        else:
            rot = rotate_around_x(angle)
        for i in range(len(self.pars)):
            self.pars[i] = self.pars[i] @ rot

    def cam_matrix(self):
        u"""
        Функция, перемещающая камеру в начало координат
        (матрицы перемещения)
        """
        x, y, z, w = self.position
        mt1 = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

        rx, ry, rz, w = self.pars[2]
        fx, fy, fz, w = self.pars[0]
        ux, uy, uz, w = self.pars[1]
        mt2 = np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])
        return mt1 @ mt2
