#!/usr/bin/env python3

# Created by: Lucas LeBlanc
# Created on: Nov 2022
# This program finds the volume of a triangle

import math


def triangle_volume_calculation(base, height, length):
    # This function calculates the volume of the triangle

    volume = math.pi * base * height * length

    return volume


def main():
    # This function gets the base, height, and length from the user

    base_from_user = input("Enter the base of the triangle (cm): ")
    height_from_user = input("Enter the height of the triangle (cm): ")
    length_from_user = input("Enter length of the triangle (cm): ")
    
    try:
        base_from_user = int(base_from_user)
        height_from_user = int(height_from_user)
        length_from_user = int(length_from_user)

        # Call function
        final_volume = triangle_volume_calculation(base_from_user, height_from_user, length_from_user)
        print(
            "\nThe volume of a triangle with the base of {0} cm, the height of {1}, and length of {2} cm is {3} cm³.".format(
                base_from_user, height_from_user, length_from_user, final_volume
            )
        )
    except Exception:
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
