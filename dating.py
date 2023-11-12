#!/usr/bin/env python3
# Created By: Ishami Sebgoya
# Date: November 12, 2023
# This program checks to see if the user is able to date their grandchild


def main():
    try:
        user_age = float(input("Enter a number: "))

        if user_age >= 26 and user_age <= 39:
            print(f"{user_age} is a valid  age")
            print("You can date my grandchild")
        else:
            print(f"{user_age} is not the right age for our grandchild")
            print("You can't date my grandchild")
    except ValueError:
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()
