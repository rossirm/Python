class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.bottom = self.top + self.height
        self.right = self.left + self.width

    def is_inside(self, other_rectangle):
        is_in_left = self.left >= other_rectangle.left
        is_in_right = self.right <= other_rectangle.right
        is_in_top = self.top >= other_rectangle.top
        is_in_bottom = self.bottom <= other_rectangle.bottom
        return is_in_left and is_in_right and is_in_top and is_in_bottom


def build_rectangle():
    coordinates = list(map(float, input().split(' ')))
    return Rectangle(*coordinates)


first = build_rectangle()
second = build_rectangle()

print('Inside' if first.is_inside(second) else 'Not inside')
