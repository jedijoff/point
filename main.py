# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.getx() - x, self.gety() - y)

    def distance_from_point(self, point):
        x_1 = self.getx()
        y_1 = self.gety()
        x_2 = point.getx()
        y_2 = point.gety()
        return math.hypot(x_1 - x_2, y_1 - y_2)


class Triangle(Point):

    def __init__(self, vertice1, vertice2, vertice3):
        Point.__init__(self)
        self.__x1 = vertice1.getx()
        self.__y1 = vertice1.gety()
        self.__x2 = vertice2.getx()
        self.__y2 = vertice2.gety()
        self.__x3 = vertice3.getx()
        self.__y3 = vertice3.gety()
        self.__len1 = math.hypot(self.__x1 - self.__x2, self.__y1 - self.__y2)
        self.__len2 = math.hypot(self.__x2 - self.__x3, self.__y2 - self.__y3)
        self.__len3 = math.hypot(self.__x3 - self.__x1, self.__y3 - self.__y1)


    def perimeter(self):
        return self.__len1 + self.__len2 + self.__len3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
