import logging
import os
import sys

import pytest


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point with coordinates: {(self.x, self.y)}'


class PointsWithCoordinates:

    def __init__(self, points_coordinates):
        self.points_coordinates = points_coordinates
        self.points = []

    def set_points_coords(self):
        for point_coord in self.points_coordinates:
            x, y = point_coord
            self.points.append(Point(x, y))

    def set_points_coords_generator_example(self):
        for point_coord in self.points_coordinates:
            x, y = point_coord
            yield Point(x, y)


class TestPointsWithCoordinates:

    def setup_class(self):
        self.working_dir = os.getcwd()
        self.coordinates = [(1, 2), (1, 3), (1, 5), (5, 5), (4, 2)]

    def test_points_with_x_1(self):
        points_with_coordinates = PointsWithCoordinates(self.coordinates)
        generator = points_with_coordinates.set_points_coords_generator_example()
        for item in generator:
            print(item)
        assert len(points_with_coordinates.points) == len(self.coordinates)
        points_with_x_1 = 0
        for point in points_with_coordinates.points:
            if point.x == 1:
                points_with_x_1 += 1
        assert points_with_x_1 == 3

    # @pytest.mark.xfail(reason="points with y 5 not equals 3")
    def test_points_with_y_5(self):
        points_with_coordinates = PointsWithCoordinates(self.coordinates)
        points_with_coordinates.set_points_coords()
        assert len(points_with_coordinates.points) == len(self.coordinates)
        points_with_y_5 = 0
        for point in points_with_coordinates.points:
            if point.y == 5:
                points_with_y_5 += 1
        if points_with_y_5 != 3:
            pytest.xfail("Failed because points with y==5 is not 3")
        # assert points_with_y_5 == 3

    @pytest.mark.skip(reason="no point with y 6")
    def test_points_with_y_6(self):
        points_with_coordinates = PointsWithCoordinates(self.coordinates)
        points_with_coordinates.set_points_coords()
        assert len(points_with_coordinates.points) == len(self.coordinates)
        points_with_y_6 = 0
        for point in points_with_coordinates.points:
            if point.y == 6:
                points_with_y_6 += 1
        # if points_with_y_6 == 0:
        #     pytest.skip("Failed because no point with y 6")
        assert points_with_y_6 > 0

    @pytest.mark.skipif(sys.platform != "Linux", reason='check linux path won\'t work in Windows')
    def test_linux_path(self):
        assert os.path.exists("/net/mucfs/project")

    @pytest.mark.parametrize("point_x, point_y", [(1, 3), (1, 4), (1, 6), (5, 6), (4, 3)])
    def test_points_coordinates(self, point_x, point_y):
        print(point_x, point_y)

    @classmethod
    def teardown_class(cls):
        logging.info("finished class: {} execution".format(cls.__name__))

