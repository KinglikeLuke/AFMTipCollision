from objects import Sample
from objects import Tip
import numpy as np

class Collision(Sample):
    def __init__(self, points, point_loc, resolution):
        super.__init__(points, point_loc, resolution)

    def check_for_collision(self, tip_x, tip_y):
        return self.landscape[tip_x] > tip_y

    def move_tip(self, corners):
        """
        Makes a Tipshape and moves it along the landscape
        :param corners: 2d array, outline of the Tip (as coordinate pairs)
        :return: path
        """
        _Tip = Tip(corners)

        low_point_x = corners[np.argmin(corners[:, 1]), 0]
        left_point_x = min(corners[0,:])
        right_point_x = max(corners[0,:])
        start_offset = min(self.landscape_coordinates) - low_point_x
        end_offset = max(self.landscape_coordinates) - low_point_x
        movements = np.arange(start_offset, end_offset, self.resolution)
        # Stich two arrays together so that their fixed point is the low point (that is set on the grid)
        tip_coordinates = np.append(np.arange(low_point_x, left_point_x, -self.resolution)[::-1],   # Must be reversed
                                    np.arange(low_point_x, right_point_x, self.resolution)[1:])     # To avoid doubling
        for x in movements:
            tip_x = tip_coordinates + x
            tip_y = _Tip.shape(tip_coordinates)
            self.check_for_collision(tip_x, tip_y)


