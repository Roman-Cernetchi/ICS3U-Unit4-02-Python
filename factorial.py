#!/usr/bin/env python3
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program finds the factorial of a number


def main():
    # This function calculates the factorial of a number

    # Input
    positive_integer_string = input("Enter the positive integer you chose: ")
    print("")

    # process
    try:
        positive_integer = int(positive_integer_string)

        assert positive_integer > 0

        loop_counter = 1
        number_sum = 1

        while loop_counter < positive_integer:
            loop_counter = loop_counter + 1
            number_sum = number_sum * loop_counter

        print(number_sum)

    except AssertionError:
        print("Integer wasn't positive")
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
