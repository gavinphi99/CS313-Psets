#  File: MagicSquare.py

#  Description:

#  Student's Name: Phillip Gavino

#  Student's UT EID: pag2529

#  Partner's Name: Jack Qiao

#  Partner's UT EID: jq3838

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 9/3/2021

#  Date Last Modified: 9/3/2021

import sys
import math


# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square(n):
    num = 1
    magic_square = [[0 for k in range(n)] for l in range(n)]  # creates matrix
    for i in range(n):
        for j in range(n):
            magic_square[n-1][math.ceil(n/2)] = 1
            if (n == 1):
                return magic_square
            if (magic_square.index(num) < n):
                num = num + 1
                magic_square[i + 1][j + 1] = num
            elif ()


    pass


# Print the magic square in a neat format where the numbers
# are right justified. This is a helper function.
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square(magic_square):
    pass


# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# This is a helper function.
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square(magic_square):
    pass


# Input: square is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the magic square
#         if n is outside the range return 0
def sum_adjacent_numbers(square, n):
    pass


def main():


# read the input file from stdin

# create the magic square

# print the sum of the adjacent numbers
    pass

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
