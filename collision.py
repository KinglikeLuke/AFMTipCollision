import matplotlib.pyplot as plt

from objects import Sample
from objects import Tip
import numpy as np
from matplotlib.animation import FuncAnimation
import functools


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

        return min(differences)

    def move_tip(self, corners, do_animation=False):
        """
        Makes a Tipshape and moves it along the landscape
        :param corners: 2d array, outline of the Tip (as coordinate pairs)
        :param do_animation: bool, whether a animation of the tip moving should be played
        :return: path
        """
        _Tip = Tip(corners)

        low_point = np.argmin(corners[:, 1])
        low_point_x = corners[low_point, 0]
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
            y_movements.append(min(tip_y))
        if do_animation:
            ani = self.animation(corners, x_movements + low_point_x, y_movements)
            return x_movements + low_point_x, y_movements, ani
        return x_movements + low_point_x, y_movements

    def animation(self, corners, x_move, y_move):
        fig, ax = plt.subplots()
        ln, = plt.plot([], [], 'ro', ls='-')
        update_corners = functools.partial(self.update, corners=corners, x_data=x_move, y_data=y_move, ln=ln,)
        init_corners = functools.partial(self.init, ax=ax, ln=ln, )
        ani = FuncAnimation(fig, update_corners, frames=range(len(x_move)), init_func=init_corners, blit=True)
        return ani

    def init(self, ax, ln):
        ax.set_xlim(min(self.landscape_coordinates) - 10*self.resolution,
                         max(self.landscape_coordinates) + 10*self.resolution)
        ax.set_ylim(min(self.landscape) - 10*self.resolution,
                         max(self.landscape) + 10*self.resolution)
        ax.plot(self.landscape_coordinates, self.landscape)

        return ln,

    def update(self, frame, corners, x_data, y_data, ln):
        ln.set_data(x_data[frame], y_data[frame])
        return ln,






