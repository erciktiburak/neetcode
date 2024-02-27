""" Implement the Adapter design pattern.

The Adapter is a structural design pattern that allows incompatible interfaces to work together. It wraps an existing class with a new interface so that it becomes compatible with the client's interface.

You are given completed SquareHole, Square and Circle classes. A Square fits into a SquareHole if the Square's side length is less than or equal to the SquareHole's length. A Circle has a radius and a Circle fits into a SquareHole if the Circle's diameter is less than or equal to the SquareHole's length.

Complete the implementation of the CircleToSquareAdapter class such that it adapts a Circle to a Square.
 """
from math import sqrt

class Square:
    def __init__(self, sideLength=0.0):
        self.sideLength = sideLength

    def getSideLength(self) -> float:
        return self.sideLength
    
class SquareHole:
    def __init__(self, sideLength: float):
        self.sideLength = sideLength

    def canFit(self, square: Square):
        return self.sideLength >= square.getSideLength()

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def getRadius(self):
        return self.radius

class CircleToSquareAdapter(Square):
    def __init__(self, circle: Circle):
        # Calculate the side length of the square that can fit the circle
        # The diagonal of the square should be equal to the diameter of the circle
        self.sideLength = 2 * circle.getRadius()

    def getSideLength(self) -> float:
        return self.sideLength

# Example usage
def adapter_pattern():
    squareHole = SquareHole(5)

    square = Square(5)
    print(squareHole.canFit(square))  # Output: True

    circle = Circle(2.6)
    circleAdapter = CircleToSquareAdapter(circle)
    print(squareHole.canFit(circleAdapter))  # Output: False

adapter_pattern()
