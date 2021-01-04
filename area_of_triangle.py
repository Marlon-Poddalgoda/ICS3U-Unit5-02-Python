#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on January 2021
# This program calculates the area of a triangle


def areaOfTriangle(base, height):
    # this function calculates the area of a triangle

    # process
    area_of_triangle = (base * height) / 2

    # output
    print("The area of this triangle is {} m².".format(area_of_triangle))


def main():
    # this function gets base and height

    # input
    base_of_triangle = input("Enter the base of the triangle (m): ")
    height_of_triangle = input("Enter the height of the triangle (m): ")
    print("")

    try:
        base_int = int(base_of_triangle)
        height_int = int(height_of_triangle)

        if base_int > 0 and height_int > 0:
            # call function
            areaOfTriangle(base_int, height_int)
        else:
            # output
            print("Enter a positive integer for both values, try again.")

    except Exception:
        # output
        print("Enter a number for both values, try again.")


if __name__ == "__main__":
    main()
