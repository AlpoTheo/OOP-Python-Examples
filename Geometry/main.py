from shape import Shape
from rectangle import Rectangle
from square import Square
from triangle import Triangle
from cube import Cube
from ellipse import Ellipse
from circle import Circle

shape1 = Shape()
rectangle1 = Rectangle(2,3)
square1 = Square(4)
triangle1 = Triangle(4,5)
cube1 = Cube(6)
ellipse1 = Ellipse(2,5)
ellipse1.change_PI(3.2)
circle1 = Circle(2)

for shape in [shape1,rectangle1,square1,triangle1,cube1,ellipse1,circle1]:
    print(shape)

"""
example output:

Shape:Shape,area:None
Shape:Rectangle,area:6
Shape:Square,area:16
Shape:Triangle,area:10.0
Shape:Cube,volume:216
Shape:Ellipse,area:32.0
Shape:Circle,area:12.8

"""