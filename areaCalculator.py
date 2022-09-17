"""A simple area calculator that will ask the user to choose a shape, calculate the area of the shape, and return the area of the chosen shape."""

import math


def greeting(self):
    print("Hello there! I am AreaCalculator 1.0. Please select a shape and I'll calculate the area for you.")


def chooseShape(self):
    shape_choice = input(
        "Enter S for a square, C for circle, or T for triangle!")
    return shape_choice.lower()


def findArea(self, shape_choice):
    if shape_choice == "c":
        radius = float(input("Enter the radius of the circle."))
        cArea = math.pi * (radius**2)
