# -*- coding: utf-8 -*-
import math

import numpy as np
import pygame as pg
import matrix as mt

u"""
Файл, в котором мы задаем объекты
"""


class Object3d:
    def __init__(self, render):
        u"""
        Передаем вершины и грани единичного куба
        """
        self.render = render
        self.vertexes = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
                                  (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])
        self.faces = np.array([(0, 1, 2, 3), (1, 5, 6, 2), (3, 2, 6, 7), (0, 1, 5, 4), (4, 5, 6, 7), (0, 4, 7, 3)])

    def update(self):
        u"""
        Функция отрисовки объекта
        """
        self.move()
        self.draw()

    def draw(self):
        u"""
        Функция, перемещающая вершины объекты в простраства взгляда камеры;
        создание пространства отсечения;
        выбор осей
        """
        vertexes = np.dot(self.vertexes, self.render.camera.cam_matrix())
        vertexes = np.dot(vertexes, self.render.projection.formation_of_clipping_matrix)
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        vertexes = np.dot(vertexes, self.render.projection.vertex_to_screen_matrix)
        vertexes = vertexes[:, :2]

        for face in self.faces:
            polygon = vertexes[face]
            if not np.any((polygon == self.render.HfWidth) | (polygon == self.render.HfHeight)):
                pg.draw.polygon(self.render.screen, pg.Color('white'), polygon, 3)

        for vertex in vertexes:
            if not np.any((vertex == self.render.HfWidth) | (vertex == self.render.HfHeight)):
                pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 6)

    u"""
    Функции, в котороых мы задаем функции перемещения объекта в пространстве
    """
    def move(self):
        u"""
        Функции, перманентно изменяющее положение или размеры объекта объекта
        """
        # self.move_to([0,math.sin(pg.time.get_ticks() % 0.01),0])
        self.rotate_around_x((pg.time.get_ticks() % 0.01))
        # self.rotate_around_y((pg.time.get_ticks() % 0.01))
        # self.rotate_around_z((pg.time.get_ticks() % 0.01))

    def move_to(self, pos):
        u"""
        Функция перемещения объекта
        """
        self.vertexes = self.vertexes @ mt.move_to(pos)

    def scale_change(self, scale_to):
        u"""
        Функция изменения размера
        """
        self.vertexes = self.vertexes @ mt.scale_change(scale_to)

    def rotate_around_x(self, angle):
        u"""
        Функции, вращающая объект вокруг оси x
        """
        self.vertexes = self.vertexes @ mt.rotate_around_x(angle)

    def rotate_around_y(self, angle):
        u"""
        Функции, вращающая объект вокруг оси y
        """
        self.vertexes = self.vertexes @ mt.rotate_around_y(angle)

    def rotate_around_z(self, angle):
        u"""
        Функции, вращающая объект вокруг оси z
        """
        self.vertexes = self.vertexes @ mt.rotate_around_z(angle)
