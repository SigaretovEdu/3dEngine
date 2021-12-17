import math
import numpy as np


class Projection:
    def __init__(self, render):
        NEAR = render.camera.close
        FAR = render.camera.far
        RIGHT = math.tan(render.camera.screen_par[0] / 2)
        LEFT = -RIGHT
        TOP = math.tan(render.camera.screen_par[1] / 2)
        BOTTOM = -TOP

        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP - BOTTOM)
        m22 = (FAR + NEAR) / (FAR - NEAR)
        m32 = -2 * NEAR * FAR / (FAR - NEAR)
        self.projection_matrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])

        HW, HH = render.HfWidth, render.HfHeight
        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0],
            [0, -HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]
        ])
