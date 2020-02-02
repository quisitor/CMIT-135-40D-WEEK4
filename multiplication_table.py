"""

:Student: Craig Smith
:Week-4: Loops
:Module: guess_the_number
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles
:Author: Craig Smith

Purpose
-------
The program prints a formatted multiplication chart for numbers 1-9 to the terminal

Constraints
-----------
1. Chart should reflect numbers 1 to 9
2. Chart should be well formatted/aligned in a standard table grid pattern
3. Chart should be generated using a nested for loop

"""

# Main

if __name__ == '__main__':

    products = []
    for row in range(1, 10):
        for col in range(1, 10):
            products.append(row * col)
        print(f"{products[0]:>3}{products[1]:>3}{products[2]:>3}{products[3]:>3}"
              f"{products[4]:>3}{products[5]:>3}{products[6]:>3}{products[7]:>3}"
              f"{products[8]:>3}")
        products.clear()

