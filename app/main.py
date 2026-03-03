import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return (self.x, self.y)

    def __str__(self):
        return str(self.coordinates)

    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
        else:
            new_x = self.x + other[0]
            new_y = self.y + other[1]
        result = Vector(new_x, new_y)
        return result

    def __sub__(self, other):
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
        else:
            new_x = self.x - other[0]
            new_y = self.y - other[1]
        result = Vector(new_x, new_y)
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other

        elif isinstance(other, Vector):
            new_x = self.x * other.x
            new_y = self.y * other.y
        else:
            return NotImplemented
        result = Vector(new_x, new_y)
        return result

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        if isinstance(start_point, cls) and isinstance(end_point, cls):
            vector_x = round(end_point.x - start_point.x, 2)
            vector_y = round(end_point.y - start_point.y, 2)
        else:
            return NotImplemented
        return cls(vector_x, vector_y)

    def get_length(self):
        return round(math.sqrt(self.x**2 + self.y**2), 2)

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other):
        self_len = self.get_length()
        if not isinstance(other, Vector):
            return NotImplemented
        other_len = other.get_length()
        if self_len == 0 or other_len == 0:
            return 0
        dot_product = self.x * other.x + self.y * other.y

        cos_a = max(-1.0, min(1.0, dot_product / (self_len * other_len)))

        angle_rad = math.acos(cos_a)
        return math.ceil(math.degrees(angle_rad))

    def get_angle(self):
        if self.x == 0 and self.y == 0:
            return 0
        length = self.get_length()
        cos_a = self.y / length
        angle = math.degrees(math.acos(max(-1.0, min(1.0, cos_a))))

        return int(angle)

    def rotate(self, degrees):
        radians = math.radians(degrees)

        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a

        return Vector(round(new_x, 2), round(new_y, 2))
