# -*- coding: utf-8 -*-
import math
import numpy as np


class Projection_Matrix:
    u"""
    Данный класс служит для простроения матрицы проекции, которая служит для корректного
    отображения объекта
    """

    def __init__(self, render):
        u"""
        Импорт необходимых переменных
        """
        near_clipping_plane = render.camera.close
        far_clipping_plane = render.camera.far
        right_zone = math.tan(render.height / 2)
        left_zone = - right_zone
        top_zone = math.tan(render.width / 2)
        bottom_zone = -top_zone

        self.formation_of_clipping_matrix = np.array([
            [2 / (right_zone - left_zone), 0, 0, 0],
            [0, 2 / (top_zone - bottom_zone), 0, 0],
            [0, 0, (far_clipping_plane + near_clipping_plane) / (far_clipping_plane - near_clipping_plane), 1],
            [0, 0, -2 * near_clipping_plane * far_clipping_plane / (far_clipping_plane - near_clipping_plane), 0]
        ])

        self.vertex_to_screen_matrix = np.array([
            [render.HfWidth, 0, 0, 0],
            [0, -render.HfHeight, 0, 0],
            [0, 0, 1, 0],
            [render.HfWidth, render.HfHeight, 0, 0]
        ])
