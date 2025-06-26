from polymorphism_demo import Shape, Rectengle, Circle
import math

def main():
    shapes = [
       Rectengle (10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()