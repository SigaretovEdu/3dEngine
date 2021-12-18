# -*- coding: utf-8 -*-
import numpy as np
import pygame as pg
import matrix as mt


class Object3d:
    def __init__(self, render):
        self.render = render
        self.vertexes = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
                                  (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])
        self.faces = np.array([(0, 1, 2, 3), (1, 5, 6, 2), (3, 2, 6, 7), (0, 1, 5, 4), (4, 5, 6, 7), (0, 4, 7, 3)])

    def update(self):
        self.move()
        self.draw()

    def draw(self):
        vertexes = np.dot(self.vertexes, self.render.camera.cam_matrix())
        vertexes = np.dot(vertexes, self.render.projection.projection_matrix)
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        vertexes = np.dot(vertexes, self.render.projection.to_screen_matrix)
        vertexes = vertexes[:, :2]

        for face in self.faces:
            polygon = vertexes[face]
            if not np.any((polygon == self.render.HfWidth) | (polygon == self.render.HfHeight)):
                pg.draw.polygon(self.render.screen, pg.Color('white'), polygon, 3)

        for vertex in vertexes:
            if not np.any((vertex == self.render.HfWidth) | (vertex == self.render.HfHeight)):
                pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 6)

    def move(self):
        self.rotate_around_y(-(pg.time.get_ticks() % 0.005))

    def move_to(self, pos):
        self.vertexes = self.vertexes @ mt.move_to(pos)

    def scale_change(self, scale_to):
        self.vertexes = self.vertexes @ mt.scale_change(scale_to)

    def rotate_around_x(self, angle):
        self.vertexes = self.vertexes @ mt.rotate_around_x(angle)

    def rotate_around_y(self, angle):
        self.vertexes = self.vertexes @ mt.rotate_around_y(angle)

    def rotate_around_z(self, angle):
        self.vertexes = self.vertexes @ mt.rotate_around_z(angle)