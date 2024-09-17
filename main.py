"""
Prblem Statement:
- Calculate your age based on the current year and your birth year.
- Write a program that calculates the area of a rectangle using length and width variables.
- Write a program that calculates the area of a circle.
- Write a program that calculates the area of the cube.
- Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
- Convert a given number of seconds into minutes and seconds using variables.
- Write a program that calculates the percentage.
- Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.
- Write a program that calculates the volume of a cylinder using the formula .
"""

from funs import *

while True:
    print("Select Number from  the list you want to perform:")
    print("1 : Calculate your age based on the current year.")
    print("2 : Calculates the area of a rectangle.")
    print("3 : Calculates the area of a circle.")
    print("4 : Calculates the area of the cube.")
    print("5 : Convert temperature from Fahrenheit to Celsius and vice versa.")
    print("6 : Convert seconds into minutes and seconds.")
    print("7 : Calculates the percentage.")
    print("8 : Calculates the BMI using height and weight.")
    print("9 : Calculates the volume of a cylinder.")
    print("10: Press '0' to quit.")

    num : int = input("\nEnter the Number of task you want to perform : ")
    match num:
        case "1":
            calc_age()

        case "2":
            rect_area()

        case "3":
            circle_area()

        case "4":
            cube_area()

        case "5":
            calc_temp()

        case "6":
            calc_time()

        case "7":
            calc_pecentage()

        case "8":
            calc_bmi()

        case "9":
            calc_volume()

        case "0":
            break

        case Default:
            print("Select 1 to 9 numbers, or '0' to quit.\n")
