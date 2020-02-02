"""

:Student: Craig Smith
:Week-4: Loops
:Module: countdown
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles
:Author: Craig Smith

Purpose
-------
This program counts down from 10 utilizing the "while" loop method and the
"for" loop method.

Constraints
-----------
1. Upper starting limit integer 10
2. Include a "while" loop version
3. Include a "for" loop version

"""

# Helper functions


def while_countdown(starting_number):
    """
    This function takes a number, validates its a positive integer, and prints
    the countdown to 0 to the terminal using a "while" loop.

    :param starting_number: Integer > 0
    :terminal output: Label indicating countdown method used and a printout of the countdown
    """
    print(f"Counting down from {starting_number} to 0 using a 'while loop'")
    while starting_number >= 0:
        print(starting_number)
        starting_number -= 1


def for_countdown(starting_number):
    """
    This function takes a number, validates its a positive integer, and prints
    the countdown to 0 to the terminal using a "for" loop.

    :param starting_number: Integer > 0
    :terminal output: Label indicating countdown method used and a printout of the countdown
    """
    print(f"Counting down from {starting_number} to 0 using a 'for loop'")
    for number in range(starting_number, -1, -1):
        print(number)

# Main


if __name__ == '__main__':
    while_countdown(10)
    for_countdown(10)
