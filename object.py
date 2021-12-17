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
        self.movement()
        self.draw()

    def draw(self):
        vertexes = np.dot(self.vertexes, self.render.camera.camera_matrix())
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

    def movement(self):
        pass

    def translate(self, pos):
        self.vertexes = self.vertexes @ mt.translate(pos)

    def scale(self, scale_to):
        self.vertexes = self.vertexes @ mt.scale(scale_to)

    def rotate_x(self, angle):
        self.vertexes = self.vertexes @ mt.rotate_x(angle)

    def rotate_y(self, angle):
        self.vertexes = self.vertexes @ mt.rotate_y(angle)

    def rotate_z(self, angle):
        self.vertexes = self.vertexes @ mt.rotate_z(angle)