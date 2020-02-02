"""

:Student: Craig Smith
:Week-4: Loops
:Module: two_to_the_m
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles
:Author: Craig Smith

Purpose
-------
This program calculates 2^n for 0 < n < 101 and outputs the results to the terminal.
The program answers the question: 'How high can you count on 100 fingers?'

Constraints
-----------
1. Utilizes the function 2^n for positive integers 1 to 100 inclusive
2. Utilizes a 'for loop' to perform the iterative calculations
3. Prints one answer per line to the terminal
"""

# Main

if __name__ == '__main__':

    for number in range(1, 101):
        print(f"How high you can count on {number} finger(s) = {2**number:,}")
