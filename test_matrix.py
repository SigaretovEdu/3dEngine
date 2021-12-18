from unittest import TestCase
from matrix import *


class Move_Test(TestCase):
    def test_move_to1(self):
        self.assertEqual(move_to([1, 1, 1]), ([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 1]]))

    def test_move_to2(self):
        self.assertEqual(move_to([0, 0, 0]), ([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))

    def test_move_to3(self):
        self.assertEqual(move_to([153, 1, 1000]), ([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [153, 1, 1000, 1]]))

    def test_move_to4(self):
        self.assertEqual(move_to([-1, -1, -1]), ([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-1, -1, -1, 1]]))


class RX_Test(TestCase):
    def test_rotate_around_x1(self):
        self.assertEqual(rotate_around_x(15), ([[1, 0, 0, 0], [0, -0.7596879128588213, 0.6502878401571168, 0],
                                                [0, -0.6502878401571168, -0.7596879128588213, 0], [0, 0, 0, 1]]))

    def test_rotate_around_x2(self):
        self.assertEqual(rotate_around_x(360), ([[1, 0, 0, 0], [0, -0.2836910914865273, 0.9589157234143065, 0],
                                                 [0, -0.9589157234143065, -0.2836910914865273, 0], [0, 0, 0, 1]]))

    def test_rotate_around_x3(self):
        self.assertEqual(rotate_around_x(180), ([[1, 0, 0, 0], [0, -0.5984600690578581, -0.8011526357338304, 0],
                                                 [0, 0.8011526357338304, -0.5984600690578581, 0], [0, 0, 0, 1]]))

    def test_rotate_around_x4(self):
        self.assertEqual(rotate_around_x(0), ([[1, 0, 0, 0], [0, 1.0, 0.0, 0], [0, -0.0, 1.0, 0], [0, 0, 0, 1]]))


class RY_Test(TestCase):
    def test_rotate_around_y1(self):
        self.assertEqual(rotate_around_y(15), ([[-0.7596879128588213, 0, -0.6502878401571168, 0], [0, 1, 0, 0],
                                                [0.6502878401571168, 0, -0.7596879128588213, 0], [0, 0, 0, 1]]))

    def test_rotate_around_y2(self):
        self.assertEqual(rotate_around_y(360), ([[-0.2836910914865273, 0, -0.9589157234143065, 0], [0, 1, 0, 0],
                                                 [0.9589157234143065, 0, -0.2836910914865273, 0], [0, 0, 0, 1]]))

    def test_rotate_around_y3(self):
        self.assertEqual(rotate_around_y(180), ([[-0.5984600690578581, 0, 0.8011526357338304, 0], [0, 1, 0, 0],
                                                 [-0.8011526357338304, 0, -0.5984600690578581, 0], [0, 0, 0, 1]]))

    def test_rotate_around_y4(self):
        self.assertEqual(rotate_around_y(0), ([[1.0, 0, -0.0, 0], [0, 1, 0, 0], [0.0, 0, 1.0, 0], [0, 0, 0, 1]]))


class RZ_Test(TestCase):
    def test_rotate_around_z1(self):
        self.assertEqual(rotate_around_z(15), (
        [[-0.7596879128588213, 0.6502878401571168, 0, 0], [-0.6502878401571168, -0.7596879128588213, 0, 0],
         [0, 0, 1, 0], [0, 0, 0, 1]]))

    def test_rotate_around_z2(self):
        self.assertEqual(rotate_around_z(360), (
        [[-0.2836910914865273, 0.9589157234143065, 0, 0], [-0.9589157234143065, -0.2836910914865273, 0, 0],
         [0, 0, 1, 0], [0, 0, 0, 1]]))

    def test_rotate_around_z3(self):
        self.assertEqual(rotate_around_z(180), (
        [[-0.5984600690578581, -0.8011526357338304, 0, 0], [0.8011526357338304, -0.5984600690578581, 0, 0],
         [0, 0, 1, 0], [0, 0, 0, 1]]))

    def test_rotate_around_z4(self):
        self.assertEqual(rotate_around_z(0), ([[1.0, 0.0, 0, 0], [-0.0, 1.0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))


class Scale_Test(TestCase):
    def test_scale_change1(self):
        self.assertEqual(scale_change(1), ([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))

    def test_scale_change1(self):
        self.assertEqual(scale_change(-5), ([[5, 0, 0, 0], [0, 5, 0, 0], [0, 0, 5, 0], [0, 0, 0, 1]]))

    def test_scale_change1(self):
        self.assertEqual(scale_change(100), ([[100, 0, 0, 0], [0, 100, 0, 0], [0, 0, 100, 0], [0, 0, 0, 1]]))

    def test_scale_change1(self):
        self.assertEqual(scale_change(0), ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))