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


# Question 4 Function: Using the divided difference method, print out the Hermite polynomial approximation matrix 

def hermite_poly_approx():

    # problem statement values
    a1 = 3.6
    a2 = 3.6
    a3 = 3.8
    a4 = 3.8
    a5 = 3.9
    a6 = 3.9

    b1 = 1.675
    b2 = 1.675
    b3 = 1.436
    b4 = 1.436
    b5 = 1.318
    b6 = 1.318

    # calculations
    c1 = 0
    c2 = -1.195
    c3 = (b3 - b2) / (a3 - a2)
    c4 = -1.188
    c5 = (b5 - b4) / (a5 - a4)
    c6 = -1.182

    d1 = 0
    d2 = 0
    d3 = (c3 - c2) / (a3 - a2)
    d4 = (c4 - c3) / (a4 - a2)
    d5 = (c5 - c4) / (a5 - a3)
    d6 = (c6 - c5) / (a6 - a4)

    e1 = 0
    e2 = 0
    e3 = 0
    e4 = (d4 - d3) / (a4 - a1)
    e5 = (d5 - d4) / (a5 - a2)
    e6 = (d6 - d5) / (a6 - a3)

    f1 = 0
    f2 = 0
    f3 = 0
    f4 = 0
    f5 = (e5 - e4) / (a5 - a1)
    f6 = (e6 - e5) / (a6 - a2)

    a = np.matrix([[a1, b1, c1, d1, e1, f1], [a2, b2, c2, d2, e2, f2], [a3, b3, c3, d3, e3, f3], \
                   [a4, b4, c4, d4, e4, f4], [a5, b5, c5, d5, e5, f5], [a6, b6, c6, d6, e6, f6]])
    print(a, "\n")


# Question 5 function: Using cubic spline interpolation, solve for the following using the provided data
#       part a) Find matrix A
#       part b) Vector b
#       part c) Vector c       

def cubic_spline_interpolation(x, y):

    size = len(x)
    matrix: np.array = np.zeros((size, size))
    matrix[0][0] = 1
    matrix[1][0] = x[1] - x[0]
    matrix[1][1] = 2 * ((x[1] - x[0]) + (x[2] - x[1]))
    matrix[1][2] = x[2] - x[1]
    matrix[2][1] = x[2] - x[1]
    matrix[2][2] = 2 * ((x[3] - x[2]) + (x[2] - x[1]))
    matrix[2][3] = x[3] - x[2]
    matrix[3][3] = 1

    print(matrix, "\n")


    c0 = 0
    c1 = ((3 / (x[2] - x[1])) * (y[2] - y[1])) - ((3 / (x[1] - x[0])) * (y[1] - y[0]))
    c2 = ((3 / (x[3] - x[2])) * (y[3] - y[2])) - ((3 / (x[2] - x[1])) * (y[2] - y[1]))
    c3 = 0
    c = np.array([c0, c1, c2, c3])

    print(c, "\n")


    mat = [[matrix]]
    columns = [[c0], [c1], [c2], [c3]]
    h = solve(mat, columns)

    print(h.T[0], "\n")


if __name__ == "__main__":
    np.set_printoptions(precision = 7, suppress = True, linewidth = 100)
    

    # Print Question 1

    x_1 = [3.6, 3.8, 3.9]
    y_1 = [1.675, 1.436, 1.318]
    est_x = 3.7 

    nev_meth(x_1, y_1, est_x)


    # Print Question 2 & 3

    newtons_meth_and_est()


    # Print Question 4

    hermite_poly_approx()


    # Print Question 5

    x_5 = [2, 5, 8, 10]
    y_5 = [3, 5, 7, 9]
    cubic_spline_interpolation(x_5, y_5)