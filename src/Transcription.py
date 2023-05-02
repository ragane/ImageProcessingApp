import cv2 as cv
import numpy as np
import sys


# Class used to shifting of an image's location. User select translation in axis x and y
class Translation():
    def __init__(self):
        self.tx = 0
        self.ty = 0
        self.TransformMatrix = np.float32([[1, 0, self.tx], [0, 1, self.ty]])

    def MoveImg(self, image, tx, ty):
        h, w = image.shape[:2]
        self.tx = tx
        self.ty = ty
        self.TransformMatrix = np.float32([[1, 0, self.tx], [0, 1, self.ty]])
        image = cv.warpAffine(image, self.TransformMatrix, (h, w))
        return image


# Class used to resizing of the image. User select scales factors and interpolation method
class Scalling():
    def __init__(self):
        self.fx = 0
        self.fy = 0
        self.interpolation = None

    def ScaleImg(self, image, fx, fy, interpolation):
        h, w = image.shape[:2]
        self.fx = fx
        self.fy = fy
        self.interpolation = interpolation
        image = cv.resize(image, (h * self.fx, w * self.fy), None,
                          fx = self.fx, fy = self.fy, interpolation = self.interpolation)
        return image


# Class used to rotate image with selected angle and scale
class Rotation():
    def __init__(self):
        self.angle = 0
        self.scale = 1
        self.center_point = (0, 0)
        # self.MatrixTrans = [[0,0], [0,0]]

    def RotateImg(self, image, angle, scale):
        self.angle = angle
        self.scale = scale
        h, w = image.shape[:2]
        self.center_point = (int((h - 1)/2), int((w - 1)/2))
        MatrixTrans = cv.getRotationMatrix2D((self.center_point), self.angle, self.scale)
        image = cv.warpAffine(image, MatrixTrans, (h, w))
        return image


# Class dedicated to do perspective transformation of image
class PerspectiveTrans():
    def __init__(self):
        self.TransforMatrix = None

    def GetPerspective(self, image):
        pts1 = np.float32([[50, 50], [400, 70], [387, 220], [87, 265]])
        pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
        self.TransformMatrix = cv.getPerspectiveTransform(pts1, pts2)
        image = cv.warpPerspective(image, self.TransformMatrix, (300, 300))
        return image
