from objects import Sample


class Collision(Sample):
    def __init__(self, points, point_loc, resolution):
        super.__init__(points, point_loc, resolution)
        self.landscape_coordinates =