import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


class Tip:
    def __init__(self, corners):
        """

        2d array :param corners: the coordinates of the corners  of the outline of the tip
        """
        self.corners = corners
        self.shape = interpolate.interp1d(*corners)


class Sample:
    def __init__(self, points, point_loc, resolution):
        """
        :param points:  points that outline the contour of the sample
        :param point_loc: location of the points
        :param  resolution: increment of the landscape
        :type resolution: int
        """
        try:
            points + point_loc
        except ValueError:
            raise Exception(ValueError, "step and step_len must have same length!")

        self.points = points
        self.point_loc = point_loc
        self.resolution = resolution
        self.landscape = interpolate.interp1d(self.points, self.point_loc)




