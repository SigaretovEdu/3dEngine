import math
import numpy as np

def move_to(coord):
    x2, y2, z2 = coord
    pos2=np.array([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [x2,y2,z2,1]
    ])
    return pos2


def rotate_around_x(alfa):
    pos2=np.array([
        [1,0,0,0],
        [0,math.cos(alfa),math.sin(alfa),0],
        [0,-math.cos(alfa),math.sin(alfa),0],
        [0,0,0,1]
    ])
    return pos2


def rotate_around_y(alfa):
    pos2=np.array([
        [math.cos(alfa),0,-math.sin(alfa),0],
        [0,1,0,0],
        [math.sin(alfa),0,math.cos(alfa),0],
        [0,0,0,1]
    ])
    return pos2


def rotate_around_z(alfa):
    pos2=np.array([
        [math.cos(alfa),math.sin(alfa),0,0],
        [-math.sin(alfa),math.cos(alfa),0,0],
        [0,0,1,0],
        [0,0,0,1]
    ])
    return pos2


def scale_change(a):
    pos2=np.array([
        [a,0,0,0],
        [0,a,0,0],
        [0,0,a,0],
        [0,0,0,1]
    ])
    return pos2
