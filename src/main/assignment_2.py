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


# Question 2 & 3 Function: Using Newton’s forward method, print out the polynomial approximations for degrees 1, 2, and 3 using the provided data

def newtons_meth_and_est():
    # define values given in problem statement
    x_1 = 7.2
    x_2 = 7.4
    x_3 = 7.5
    x_4 = 7.6
    y_1 = 23.5492
    y_2 = 25.3913
    y_3 = 26.8224
    y_4 = 27.4589

    # find derivatives
    first_deriv_1 = (y_2 - y_1) / (x_2 - x_1)
    first_deriv_2 = (y_3 - y_2) / (x_3 - x_2)
    first_deriv_3 = (y_4 - y_3) / (x_4 - x_3)
    second_deriv_1 = (first_deriv_2 - first_deriv_1) / (x_3 - x_1)
    second_deriv_2 = (first_deriv_3 - first_deriv_2) / (x_4 - x_2)
    third_deriv = (second_deriv_2 - second_deriv_1) / (x_4 - x_1)

    approx_table = [first_deriv_1, second_deriv_1, third_deriv]

    print(approx_table, "\n")
    
    # Using Question 2 for Question 3: Using the results from 3, approximate f(7.3)?
    est_x = 7.3
    degree_3_poly_approx = y_1 + first_deriv_1 * (est_x - x_1) + second_deriv_1 * (est_x - x_2) * (est_x - x_1)\
          + third_deriv * (est_x - x_3) * (est_x - x_2) * (est_x - x_1)

    print(degree_3_poly_approx, "\n")


if __name__ == "__main__":
    np.set_printoptions(precision = 7, suppress = True, linewidth = 100)
    

    # Print Question 1
    x = [3.6, 3.8, 3.9]
    y = [1.675, 1.436, 1.318]
    est_x = 3.7 

    nev_meth(x, y, est_x)


    # Print Question 2 & 3
    newtons_meth_and_est()