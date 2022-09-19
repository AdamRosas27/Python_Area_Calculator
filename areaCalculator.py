"""A simple area calculator that will ask the user to choose a shape, calculate the area of the shape, and return the area of the chosen shape. WORK IN PROGRESS"""
# Imports the math module to be able to use pi
import math

# Shape class


class Shape:

    # Greeting method that will welcome the user
    def greeting():
        print("Hello there! I am AreaCalculator 1.0. Please select a shape and I'll calculate the area for you.")

    # Method that prompts the user to enter a letter to choose which shape they want
    def chooseShape():
        shape_choice = input(
            "Enter S for a square, C for circle, or T for triangle!")
        return shape_choice.lower()

    # Method that takes in the user input and make sure the input is valid, if it is it will do the calculations for the area, if not it will throw an exception
    def findArea():
        if shape_choice == "c":
            radius = float(input("Enter the radius of the circle."))
            cArea = math.pi * (radius**2)
            return ("The area of the circle is: {cArea}".format(cArea))

# Circle class


class Circle:

    # Triangle class
