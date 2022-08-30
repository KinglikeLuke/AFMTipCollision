from objects import Sample
from objects import Tip
import numpy as np


class Collision(Sample):
    def __init__(self, points, point_loc, resolution):
        super().__init__(points, point_loc, resolution)

    def check_distance(self, tip_x, tip_y):
        """
        Determines the smallest distance (negative distances being the smallest) between tip and sample and returns it
        :param tip_x: x-coordinates of the tip
        :param tip_y: y-coordinates of the tip
        :return: minimal distance
        """
        # Make sure that only the tip above the sample is checked
        low_bound = tip_x >= min(self.point_loc)
        high_bound = tip_x <= max(self.point_loc)
        proper_bound = low_bound & high_bound

        differences = tip_y[proper_bound] - self.landscape_func(tip_x[proper_bound])
        contact_difference = tip_y[np.argmin(differences)]
        return contact_difference

    def move_tip(self, corners):
        """
        Makes a Tipshape and moves it along the landscape
        :param corners: 2d array, outline of the Tip (as coordinate pairs)
        :return: path
        """
        _Tip = Tip(corners)

        low_point_x = corners[np.argmin(corners[:, 1]), 0]
        left_point_x = min(corners[:, 0])
        right_point_x = max(corners[:, 0])
        start_offset = min(self.landscape_coordinates) - low_point_x
        end_offset = max(self.landscape_coordinates) - low_point_x
        x_movements = np.arange(start_offset, end_offset, self.resolution)
        # Stich two arrays together so that their fixed point is the low point (that is set on the grid)
        # Could make this with linspace because exact location does not matter
        tip_coordinates = np.append(np.arange(low_point_x, left_point_x, -self.resolution)[::-1],   # Must be reversed
                                    np.arange(low_point_x, right_point_x, self.resolution)[1:])     # To avoid doubling

        tip_y = _Tip.shape(tip_coordinates)     # get initial position of the tip
        y_movements = []
        for x in x_movements:                     # move it
            tip_x = tip_coordinates + x
            distance = self.check_distance(tip_x, tip_y)
            tip_y = tip_y - distance            # correct the distance so the sample is always in contact
            y_movements.append(distance)

        return y_movements
            


