import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


class Tip:
    def __init__(self, corners):
        """

        2d array :param corners: the coordinates of the corners  of the outline of the tip
        """
        self.corners = corners
        self.shape = interpolate.interp1d(corners[:, 0], corners[:, 1])


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
        self.landscape, self.landscape_coordinates = self.make_landscape()

    def make_landscape(self):
        left_edge = np.min(self.point_loc)
        right_edge = np.max(self.point_loc)
        pixel_count = (right_edge - left_edge) / self.resolution # hinfällig wegen arange statt linspace
        landscape_coordinates = np.arange(left_edge, right_edge, self.resolution)
        landscape = self.landscape_func(landscape_coordinates)
        return landscape, landscape_coordinates
