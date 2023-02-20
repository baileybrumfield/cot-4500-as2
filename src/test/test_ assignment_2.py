# Name: Bailey Brumfield
# Date: 2/19/2023
# Professor: Juan Parra
# Asignment: Assignment 2


#import required packages

import numpy as np
from scipy.linalg import solve


# Question 1 Function: Using Neville’s method, find the 2nd degree interpolating value for f(3.7) for the provided data

def nev_meth(x, y, est_x):
    size = len(x)
    matrix = np.zeros((size, size))

    for index, row in enumerate(matrix):
        row[0] = y[index]
    
    num_points = len(x)
    for i in range(1, num_points):
        for j in range(1, i + 1):
            first_prod = (est_x - x[i - j]) * matrix[i][j - 1]
            second_prod = (est_x - x[i]) * matrix[i - 1][j - 1]

            denom = x[i] - x[i - j]

            constant = (first_prod - second_prod) / denom

            matrix[i][j] = constant
    
    print(matrix[num_points - 1][num_points - 1], "\n")

if __name__ == "__main__":
    np.set_printoptions(precision = 7, suppress = True, linewidth = 100)
    
    # Print Question 1
    x = [3.6, 3.8, 3.9]
    y = [1.675, 1.436, 1.318]
    est_x = 3.7 

    nev_meth(x, y, est_x)