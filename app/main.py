import math
from typing import Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            x_coord=self.x_coord + other.x_coord,
            y_coord=self.y_coord + other.y_coord
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            x_coord=self.x_coord - other.x_coord,
            y_coord=self.y_coord - other.y_coord
        )

    def __mul__(self, other: "Vector") -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x_coord * other, self.y_coord * other)
        elif isinstance(other, Vector):
            return self.x_coord * other.x_coord + self.y_coord * other.y_coord
        else:
            raise TypeError

    def dot(self, other: "Vector") -> float:
        return self.x_coord * other.x_coord + self.y_coord * other.y_coord

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x_coord ** 2 + self.y_coord ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            x_coord=self.x_coord / length,
            y_coord=self.y_coord / length
        )

    def angle_between(self, other: "Vector") -> int:
        dot = self.dot(other)
        len_self = self.get_length()
        len_other = other.get_length()
        cos_a = dot / (len_self * len_other)
        angle_rad = math.acos(max(-1, min(1, cos_a)))  # avoid domain error
        return round(math.degrees(angle_rad))

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x_coord * cos_a - self.y_coord * sin_a
        new_y = self.x_coord * sin_a + self.y_coord * cos_a
        return Vector(new_x, new_y)
