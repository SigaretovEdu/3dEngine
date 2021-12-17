import math
import numpy as np

class Projection_Matrix:
    def __init__(self,render):
        # Тут всё импортируется из класса камера, так что названия поменяешь если надо
        near_clipping_plane=render.camera.near_plane
        far_clipping_plane = render.camera.far_plane
        right_zone = math.tan(render.camera.h_fov/2)
        left_zone =- right_zone
        top_zone = math.tan(render.camera.v_fov/2)
        bottom_zone = -top_zone

        self.formation_of_clipping_matrix=np.array([
            [2/(right_zone-left_zone), 0, 0, 0],
            [0, 2/(top_zone-bottom_zone),0,0],
            [0,0,(far_clipping_plane+near_clipping_plane)/(far_clipping_plane-near_clipping_plane),1],
            [0,0,-2*near_clipping_plane*far_clipping_plane/(far_clipping_plane-near_clipping_plane),0]
        ])

        self.vertex_to_screen_matrix = np.array([
            [render.H_WIDTH,0,0,0],
            [0,-render.H_HIGHT,0,0],
            [0,0,1,0],
            [H_WIDTH,H_HIGHT,0,0]
        ])
