#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: November 2020
# this program finds area and perimeter of a circle
import math


def main():
    # this program finds area and perimeter of a circle

    # input
    radius = 15

    # process
    area = (math.pi*(radius)**2)
    perimeter = (2*math.pi*(radius))

    # output
    print("If a circle has a radius of 15mm:")
    print()
    print("Area is {} mm².".format(area))
    print("Perimeter is {} mm.".format(perimeter))


if __name__ == "__main__":
    main()
