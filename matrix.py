# -*- coding: utf-8 -*-
import math
import numpy as np

u"""
Файл с функциями, который формирует необходимую матрицу
в зависимости от входных параметров
"""
def move_to(coord):
    u""" Данная функция строит матрицу перемещений в пространстве по заданным координатам"""
    x2, y2, z2 = coord
    pos2=np.array([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [x2,y2,z2,1]
    ])
    return pos2


def rotate_around_x(alfa):
    u""" Данная функция строит матрицу вращения вокруг оси x по заданным координатам"""
    pos2=np.array([
        [1,0,0,0],
        [0,math.cos(alfa),math.sin(alfa),0],
        [0,-math.cos(alfa),math.sin(alfa),0],
        [0,0,0,1]
    ])
    return pos2


def rotate_around_y(alfa):
    u""" Данная функция строит матрицу вращения вокруг оси y по заданным координатам"""
    pos2=np.array([
        [math.cos(alfa),0,-math.sin(alfa),0],
        [0,1,0,0],
        [math.sin(alfa),0,math.cos(alfa),0],
        [0,0,0,1]
    ])
    return pos2


def rotate_around_z(alfa):
    u""" Данная функция строит матрицу вращения вокруг оси z по заданным координатам"""
    pos2=np.array([
        [math.cos(alfa),math.sin(alfa),0,0],
        [-math.sin(alfa),math.cos(alfa),0,0],
        [0,0,1,0],
        [0,0,0,1]
    ])
    return pos2


def scale_change(a):
    u""" Данная функция строит матрицу изменения размера объекта в a раз"""
    pos2=np.array([
        [a,0,0,0],
        [0,a,0,0],
        [0,0,a,0],
        [0,0,0,1]
    ])
    return pos2
